# -*- coding: utf-8 -*-
# Copyright (c) 2018, John Vincent Fiel and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.background_jobs import enqueue


class OCRReceipt(Document):
    def validate(self):
        if self.file:
            frappe.publish_realtime(event='msgprint',
                                    message='Generating...',
                                    user=frappe.session.user)

            import os
            inputFilepath = self.file
            filename_w_ext = os.path.basename(inputFilepath)
            filename, file_extension = os.path.splitext(filename_w_ext)

            enqueue("erpnext_ocr.erpnext_ocr.xml_reader.get_xml", queue='long',
                    docname=self.name,filename=filename)
        else:
            frappe.publish_realtime(event='msgprint',
                                    message='Please upload a file and save to generate xml.',
                                    user=frappe.session.user)

