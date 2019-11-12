# -*- coding: utf-8 -*-
# Copyright (c) 2018, John Vincent Fiel and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

def create_ocr_reads():
    if frappe.flags.test_ocr_reads_created:
        return

    frappe.set_user("Administrator")
    doc = frappe.get_doc({
        "doctype": "OCR Read",
        "file_to_read":"sample1.jpg",
        "language": "eng"
    }).insert()

    doc = frappe.get_doc({
        "doctype": "OCR Read",
        "file_to_read":"sample2.pdf",
        "language": "eng"
    }).insert()

    frappe.flags.test_ocr_reads_created = True


class TestOCRRead(unittest.TestCase):
    def setUp(self):
        create_ocr_reads()

    def tearDown(self):
        frappe.set_user("Administrator")

    def test_ocr_read_list(self):
        # frappe.set_user("test1@example.com")
        frappe.set_user("Administrator")
        res = frappe.get_list("OCR Read", filters=[["OCR Read", "file_to_read", "like", "sample%"]], fields=["name", "file_to_read"])
        self.assertEquals(len(res), 2)
        files_to_read = [r.file_to_read for r in res]
        self.assertTrue("sample1.jpg" in files_to_read)
        self.assertTrue("sample2.pdf" in files_to_read)

