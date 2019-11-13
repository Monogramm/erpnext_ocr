# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest, os

import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

from erpnext_ocr.erpnext_ocr.doctype.ocr_read.ocr_read import read_document

class TestTesseract(unittest.TestCase):
    def test_read_document_image(self):
        recognized_text = read_document(os.path.join(os.path.dirname(__file__),
                                        "test_data", "sample1.jpg"),
                            "eng")

        # print(recognized_text)

        self.assertTrue("The quick brown fox" in recognized_text)
        self.assertTrue("jumped over the 5" in recognized_text)
        self.assertTrue("lazy dogs!" in recognized_text)
        self.assertFalse("And an elephant!" in recognized_text)

        file = open(os.path.join(os.path.dirname(__file__), "test_data", "sample1_output.txt"), "r")
        expected_text = file.read()

        self.assertTrue(recognized_text == expected_text)

    def test_read_document_pdf(self):
        recognized_text = read_document(os.path.join(os.path.dirname(__file__),
                                        "test_data", "sample2.pdf"),
                            "eng")

        # print(recognized_text)

        self.assertTrue("Python Basics" in recognized_text)
        self.assertFalse("Java" in recognized_text)

