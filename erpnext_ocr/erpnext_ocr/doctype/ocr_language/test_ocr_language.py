# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals

import frappe
import unittest

from erpnext_ocr.erpnext_ocr.doctype.ocr_language.ocr_language import lang_available, check_language, \
    get_current_language


def create_test_data():
    # Create usual user
    if not frappe.db.exists("User", "test_user@example.com"):
        test_user = frappe.new_doc("User")
        test_user.name = 'test_user'
        test_user.first_name = 'test_user'
        test_user.email = 'test_user@example.com'
        test_user.language = "en"
        test_user.insert(ignore_permissions=True)


def delete_test_data():
    if frappe.db.exists("User", "test_user@example.com"):
        # test_user = frappe.get_doc('User', "test_user@example.com")
        # test_user.remove_roles("System Manager")
        # test_user.delete()
        frappe.db.sql("""delete from `tabUser` where email='test_user@example.com'""")  # ValidationError without SQL
        frappe.db.sql("""delete from `tabEmail Queue`""")


class TestOCRLanguage(unittest.TestCase):
    def setUp(self):
        frappe.set_user("Administrator")
        if not frappe.db.exists("OCR Language", "sin"):
            frappe.get_doc({
                "doctype": "OCR Language",
                "code": "sin",
                "lang": "si"
            }).insert()
        frappe.flags.test_ocr_language_created = True
        create_test_data()
        if not frappe.db.exists("User", "admin@example.com"):
            test_user = frappe.new_doc("User")
            test_user.name = 'admin'
            test_user.first_name = 'admin'
            test_user.email = 'admin@example.com'
            test_user.language = "en"
            test_user.insert(ignore_permissions=True)

    def tearDown(self):
        if frappe.flags.test_ocr_language_created:
            frappe.set_user("Administrator")
            frappe.get_doc("OCR Language", "sin").delete()
        frappe.flags.test_ocr_language_created = False
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
        self.assertEqual("eng", get_current_language("test_user@example.com"))

    def test_get_current_language_admin(self):
        self.assertEqual("eng", get_current_language("admin@example.com"))

    def test_ocr_language(self):
        sin_lang = frappe.get_doc("OCR Language", "sin")
        if sin_lang.is_supported == 'No':
            sin_lang.type_of_ocr = "Best"
            sin_lang.download_tesseract()
            self.assertEqual(sin_lang.is_supported, "Yes")