# -*- coding: utf-8 -*-
# Copyright (c) 2018, John Vincent Fiel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from erpnext_ocr.erpnext_ocr.doctype.ocr_language.ocr_language import lang_is_support
from frappe.model.document import Document

import os
import io


class OCRRead(Document):
    def read_image(self):
        message = read_document(self.file_to_read, self.language or 'eng')

        self.read_result = message
        self.save()
        return message


@frappe.whitelist()
def read_document(path, lang='eng'):
    """Call Tesseract OCR to extract the text from a document."""
    from PIL import Image
    import requests
    import pytesseract

    if path is None:
        return None

    if not lang_is_support(lang):
        frappe.msgprint(frappe._("The selected language is not available. Please contact your administrator."),
                        raise_exception=True)

    if path.startswith('/assets/'):
        # from public folder
        fullpath = os.path.abspath(path)
    elif path.startswith('/files/'):
        # public file
        fullpath = frappe.get_site_path() + '/public' + path
    elif path.startswith('/private/files/'):
        # private file
        fullpath = frappe.get_site_path() + path
    elif path.startswith('/'):
        # local file (mostly for tests)
        fullpath = os.path.abspath(path)
    else:
        # external link
        fullpath = requests.get(path, stream=True).raw

    text = " "

    if path.endswith('.pdf'):
        from wand.image import Image as wi
        pdf = wi(filename=fullpath, resolution=300)
        pdf_image = pdf.convert('jpeg')
        i = 0
        size = len(pdf_image.sequence)
        for img in pdf_image.sequence:
            img_page = wi(image=img)
            image_blob = img_page.make_blob('jpeg')

            recognized_text = " "

            image = Image.open(io.BytesIO(image_blob))
            recognized_text = pytesseract.image_to_string(image, lang)
            text = text + recognized_text

            frappe.publish_realtime("ocr_progress_bar", {"progress": [i, size]})
            i += 1

    else:
        frappe.publish_realtime("ocr_progress_bar", {"progress": "0"}, user=frappe.session.user)

        image = Image.open(fullpath)

        text = pytesseract.image_to_string(image, lang=lang)

    text.split(" ")

    return text


def force_attach_file_doc(filename, name):
    """Alternative to 'File Upload Disconnected. Please try again.'"""
    file_url = "/private/files/" + filename

    attachment_doc = frappe.get_doc({
        "doctype": "File",
        "file_name": filename,
        "file_url": file_url,
        "attached_to_name": name,
        "attached_to_doctype": "OCR Read",
        "old_parent": "Home/Attachments",
        "folder": "Home/Attachments",
        "is_private": 1
    })
    attachment_doc.insert()

    frappe.db.sql(
        """UPDATE `tabOCR Read` SET file_to_read=%s WHERE name=%s""", (file_url, name))