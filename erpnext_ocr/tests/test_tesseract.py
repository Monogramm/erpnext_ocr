# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals

import locale
import unittest
import os

import frappe

from erpnext_ocr.erpnext_ocr.doctype.ocr_read.ocr_read import read_document


class TestTesseract(unittest.TestCase):
    def test_read_document_path_none(self):
        locale.setlocale(locale.LC_ALL, 'C')
        recognized_text = read_document(None, "eng")

        self.assertIsNone(recognized_text)

    def test_read_document_lang_not_supported(self):
        locale.setlocale(locale.LC_ALL, 'C')
        self.assertRaises(frappe.ValidationError, read_document,
                          os.path.join(os.path.dirname(__file__), "test_data", "sample1.jpg"),
                          "xxx")

    def test_read_document_image_http(self):
        locale.setlocale(locale.LC_ALL, 'C')
        recognized_text = read_document("https://github.com/Monogramm/erpnext_ocr/raw/develop/erpnext_ocr/tests/test_data/sample1.jpg",
                                        "eng")

        # print("recognized_text=" + recognized_text)

        self.assertIn("The quick brown fox", recognized_text)
        self.assertIn("jumped over the 5", recognized_text)
        self.assertIn("lazy dogs!", recognized_text)
        self.assertNotIn("And an elephant!", recognized_text)

    def test_read_document_image_jpg(self):
        locale.setlocale(locale.LC_ALL, 'C')
        recognized_text = read_document(os.path.join(os.path.dirname(__file__),
                                                     "test_data", "sample1.jpg"),
                                        "eng")

        # print("recognized_text=" + recognized_text)

        self.assertIn("The quick brown fox", recognized_text)
        self.assertIn("jumped over the 5", recognized_text)
        self.assertIn("lazy dogs!", recognized_text)
        self.assertNotIn("And an elephant!", recognized_text)

        file = open(os.path.join(os.path.dirname(__file__),
                                 "test_data", "sample1_output.txt"), "r")
        expected_text = file.read()

        # Trailing spaces or EOL are acceptable
        self.assertTrue(expected_text in recognized_text)

    def test_read_document_image_png(self):
        locale.setlocale(locale.LC_ALL, 'C')
        recognized_text = read_document(os.path.join(os.path.dirname(__file__),
                                                     "test_data", "Picture_010.png"),
                                        "eng")

        # print("recognized_text=" + recognized_text)

        self.assertIn("Brawn Manufacture", recognized_text)
        self.assertNotIn("And an elephant!", recognized_text)

    def test_read_document_pdf(self):
        locale.setlocale(locale.LC_ALL, 'C')
        recognized_text = read_document(os.path.join(os.path.dirname(__file__),
                                                     "test_data", "sample2.pdf"),
                                        "eng")

        # print("recognized_text=" + recognized_text)

        self.assertIn("Python Basics", recognized_text)
        self.assertNotIn("Java", recognized_text)
