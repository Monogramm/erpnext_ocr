# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
import unittest

from erpnext_ocr.erpnext_ocr.doctype.ocr_language.ocr_language import lang_available, check_language, \
    get_current_language


def create_test_data():
    # Create test user
    if not frappe.db.exists("User", "test_user_ocr@example.com"):
        test_user = frappe.new_doc("User")
        test_user.name = 'test_user_ocr'
        test_user.first_name = 'test_user_ocr'
        test_user.email = 'test_user_ocr@example.com'
        test_user.language = "en"
        test_user.insert(ignore_permissions=True)

    if not frappe.db.exists("User", "test_admin_ocr@example.com"):
        test_user = frappe.new_doc("User")
        test_user.name = 'test_admin_ocr'
        test_user.first_name = 'test_admin_ocr'
        test_user.email = 'test_admin_ocr@example.com'
        test_user.insert(ignore_permissions=True)

    if not frappe.db.exists("OCR Language", "sin"):
        frappe.get_doc({
            "doctype": "OCR Language",
            "code": "sin",
            "lang": "si"
        }).insert()

    if not frappe.db.exists("OCR Language", "uzb"):
        frappe.get_doc({
            "doctype": "OCR Language",
            "code": "uzb",
            "lang": "uz"
        }).insert()

    if not frappe.db.exists("OCR Language", "ukr"):
        frappe.get_doc({
            "doctype": "OCR Language",
            "code": "ukr",
            "lang": "uk"
        }).insert()

    frappe.flags.test_ocr_language_created = True


def delete_test_data():
    if frappe.db.exists("User", "test_user_ocr@example.com"):
        frappe.db.sql("""delete from `tabUser` where email='test_user_ocr@example.com'""")  # ValidationError without SQL
        frappe.db.sql("""delete from `tabEmail Queue`""")

    if frappe.db.exists("User", "test_admin_ocr@example.com"):
        frappe.db.sql("""delete from `tabUser` where email='test_admin_ocr@example.com'""")  # ValidationError without SQL
        frappe.db.sql("""delete from `tabEmail Queue`""")

    if frappe.flags.test_ocr_language_created:
        frappe.get_doc("OCR Language", "sin").delete()
        #frappe.db.sql("""delete from `tabOCR Language` where code='sin'""")

    if frappe.flags.test_ocr_language_created:
        frappe.get_doc("OCR Language", "uzb").delete()
        #frappe.db.sql("""delete from `tabOCR Language` where code='uzb'""")

    if frappe.flags.test_ocr_language_created:
        frappe.get_doc("OCR Language", "ukr").delete()
        #frappe.db.sql("""delete from `tabOCR Language` where code='sin_custom'""")

    frappe.flags.test_ocr_language_created = False

class TestOCRLanguage(unittest.TestCase):
    def setUp(self):
        frappe.set_user("Administrator")
        create_test_data()

    def tearDown(self):
        frappe.set_user("Administrator")
        delete_test_data()

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

    def test_get_current_language(self):
        self.assertEqual("eng", get_current_language("test_user_ocr@example.com"))

    def test_get_current_language_admin(self):
        self.assertEqual("eng", get_current_language("test_admin_ocr@example.com"))

    def test_download_tesseract_default(self):
        sin_lang = frappe.get_doc("OCR Language", "sin")
        if sin_lang.is_supported == 'No':
            sin_lang.type_of_ocr = "Default"
            sin_lang.download_tesseract()
            self.assertEqual(sin_lang.is_supported, "Yes")

    def test_download_tesseract_best(self):
        uzb_lang = frappe.get_doc("OCR Language", "uzb")
        if uzb_lang.is_supported == 'No':
            uzb_lang.type_of_ocr = "Best"
            uzb_lang.download_tesseract()
            self.assertEqual(uzb_lang.is_supported, "Yes")

    def test_download_tesseract_custom(self):
        ukr_lang = frappe.get_doc("OCR Language", "ukr")
        if ukr_lang.is_supported == 'No':
            ukr_lang.type_of_ocr = "Custom"
            self.assertRaises(frappe.ValidationError, ukr_lang.download_tesseract)
