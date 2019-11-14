# -*- coding: utf-8 -*-
# Copyright (c) 2018, John Vincent Fiel and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest
import os


def create_ocr_reads():
    if frappe.flags.test_ocr_reads_created:
        return

    frappe.set_user("Administrator")
    frappe.get_doc({
        "doctype": "OCR Read",
        "file_to_read": os.path.join(os.path.dirname(__file__),
                                     os.path.pardir, os.path.pardir, os.path.pardir,
                                     "tests", "test_data", "sample1.jpg"),
        "language": "eng"
    }).insert()

    frappe.get_doc({
        "doctype": "OCR Read",
        "file_to_read": os.path.join(os.path.dirname(__file__),
                                     os.path.pardir, os.path.pardir, os.path.pardir,
                                     "tests", "test_data", "sample2.pdf"),
        "language": "eng"
    }).insert()

    frappe.flags.test_ocr_reads_created = True


def delete_ocr_reads():
    if frappe.flags.test_ocr_reads_created:
        frappe.set_user("Administrator")

        for d in frappe.get_all("OCR Read"):
            doc = frappe.get_doc("OCR Read", d.name)
            doc.delete()

        # Delete directly in DB to avoid validation errors
        #frappe.db.sql("""delete from `tabOCR Read`""")

        frappe.flags.test_ocr_reads_created = False


class TestOCRRead(unittest.TestCase):
    def setUp(self):
        create_ocr_reads()

    def tearDown(self):
        delete_ocr_reads()

    # TODO: Read content of files and check recognised text

    #def test_ocr_read_image(self):
    #    frappe.set_user("Administrator")

    #def test_ocr_read_pdf(self):
    #    frappe.set_user("Administrator")

    def test_ocr_read_list(self):
        # frappe.set_user("test1@example.com")
        frappe.set_user("Administrator")
        res = frappe.get_list("OCR Read", filters=[
                              ["OCR Read", "file_to_read", "like", "%sample%"]], fields=["name", "file_to_read"])
        self.assertEqual(len(res), 2)
        files_to_read = [r.file_to_read for r in res]
        self.assertTrue(os.path.join(os.path.dirname(__file__),
                                     os.path.pardir, os.path.pardir, os.path.pardir,
                                     "tests", "test_data", "sample1.jpg") in files_to_read)
        self.assertTrue(os.path.join(os.path.dirname(__file__),
                                     os.path.pardir, os.path.pardir, os.path.pardir,
                                     "tests", "test_data", "sample2.pdf") in files_to_read)
