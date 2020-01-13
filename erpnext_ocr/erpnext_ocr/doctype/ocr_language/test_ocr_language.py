# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals

import frappe
import unittest

from erpnext_ocr.erpnext_ocr.doctype.ocr_language.ocr_language import lang_available, check_language


class TestOCRLanguage(unittest.TestCase):
    def test_en_lang_available(self):
        self.assertTrue(lang_available("en"))

    def test_eng_lang_available(self):
        self.assertTrue(lang_available("eng"))

    def test_osd_lang_available(self):
        self.assertTrue(lang_available("osd"))

    def test_equ_lang_available(self):
        self.assertTrue(lang_available("equ"))

    def test_666_lang_available(self):
        self.assertFalse(lang_available("666"))

    def test_en_check_language(self):
        self.assertEqual(check_language("en"), frappe._("Yes"))

    def test_eng_check_language(self):
        self.assertEqual(check_language("eng"), frappe._("Yes"))

    def test_osd_check_language(self):
        self.assertEqual(check_language("osd"), frappe._("Yes"))

    def test_equ_check_language(self):
        self.assertEqual(check_language("equ"), frappe._("Yes"))

    def test_666_check_language(self):
        self.assertEqual(check_language("666"), frappe._("No"))

    def test_creation_of_ocr_language(self):
        frappe.set_user("Administrator")
        frappe.get_doc({
            "doctype": "OCR Language",
            "lang": "en"
        }).insert()