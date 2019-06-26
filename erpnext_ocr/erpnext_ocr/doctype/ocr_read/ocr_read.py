# -*- coding: utf-8 -*-
# Copyright (c) 2018, John Vincent Fiel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

#Alternative to "File Upload Disconnected. Please try again."

#erpnext_ocr.erpnext_ocr.doctype.ocr_read.ocr_read.force_attach_file
def force_attach_file():
    filename = "Picture_010.tif"
    name = "a2cbc0186c"
    force_attach_file_doc(filename,name)

def force_attach_file_doc(filename,name):
    # file = "/private/files/"

    file_url = "/private/files/" + filename
    # file_url = "/files/" + filename

    attachment_doc = frappe.get_doc({
        "doctype": "File",
        "file_name": filename,
        # "file_url": path,
        "file_url": file_url,
        "attached_to_name": name,
        "attached_to_doctype": "OCR Read",
        "old_parent": "Home/Attachments",
        "folder": "Home/Attachments",
        "is_private": 1
        # "is_private": 0
    })
    attachment_doc.insert()

    frappe.db.sql("""UPDATE `tabOCR Read` SET file_to_read=%s WHERE name=%s""", (file_url, name))


class OCRRead(Document):
    def read_image(self):
        from PIL import Image
        import pytesseract

        fullpath = frappe.get_site_path() + self.file_to_read
        im = Image.open(fullpath)

        text = pytesseract.image_to_string(im, lang='eng')

        # print(text)
        # for t in text:
        #     print(t)
        text.split(" ")

        print(text)
        text_list = []
        string = ""
        # self.read_result = text
        # self.save()
        return text