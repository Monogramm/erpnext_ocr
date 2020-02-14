# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest


class TestOCRSettings(unittest.TestCase):
    def test_validate(self):
        ocr = frappe.get_doc("OCR Settings")
        ocr.pdf_resolution = 300
        ocr.validate()
        self.assertEqual(300, ocr.pdf_resolution)

    def test_validate_invalid_pdf_resolution(self):
        ocr = frappe.get_doc("OCR Settings")
        ocr.pdf_resolution = -1
        self.assertRaises(frappe.ValidationError, ocr.validate)

        ocr.pdf_resolution = 0
        self.assertRaises(frappe.ValidationError, ocr.validate)
