# -*- coding: utf-8 -*-
# Copyright (c) 2018, John Vincent Fiel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import os
import io

#Alternative to "File Upload Disconnected. Please try again."

#erpnext_ocr.erpnext_ocr.doctype.ocr_read.ocr_read.force_attach_file
def force_attach_file():
    filename = "Picture_010.tif"
    name = "a2cbc0186c"
    force_attach_file_doc(filename,name)

def force_attach_file_doc(filename,name):
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

    frappe.db.sql("""UPDATE `tabOCR Read` SET file_to_read=%s WHERE name=%s""", (file_url, name))


class OCRRead(Document):
    def read_image(self):
        from PIL import Image
        import requests
        import pytesseract

        path = self.file_to_read
        if path == None:
            return None

        if path.startswith('/assets/'):
            # from public folder
            fullpath = os.path.abspath(path)
        elif path.startswith('/files/'):
            # public file
            fullpath = frappe.get_site_path() + '/public' + path
        elif path.startswith('/private/files/'):
            # private file
            fullpath = frappe.get_site_path() + path
        else:
            # external link
            fullpath = requests.get(path, stream=True).raw

        lang = self.language or 'eng'

        text = " "

        if path.endswith('.pdf'):
            from wand.image import Image as wi

            # https://stackoverflow.com/questions/43072050/pyocr-with-tesseract-runs-out-of-memory
            with wi(filename = fullpath, resolution = 300) as pdf:
                pdfImage = pdf.convert('jpeg')

                for img in pdfImage.sequence:
                    with wi(image = img) as imgPage:
                        imageBlob = imgPage.make_blob('jpeg')

                        recognized_text = " "

                        im = Image.open(io.BytesIO(imageBlob))
                        recognized_text = pytesseract.image_to_string(im, lang)
                        text = text + recognized_text

        else:
            im = Image.open(fullpath)

            text = pytesseract.image_to_string(im, lang=lang)

        text.split(" ")

        self.read_result = text
        self.save()

        return text
