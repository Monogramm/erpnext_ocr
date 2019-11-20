# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt
from __future__ import unicode_literals

import locale
import unittest, os

from erpnext_ocr.erpnext_ocr.doctype.ocr_read.ocr_read import read_document

class TestTesseract(unittest.TestCase):
    def test_read_document_image(self):
        locale.setlocale(locale.LC_ALL, 'C')
        recognized_text = read_document(os.path.join(os.path.dirname(__file__),
                                        "test_data", "sample1.jpg"),
                            "eng")['message']

        # print(recognized_text)

        print("Recognized text is: " + str(recognized_text))
        self.assertTrue("The quick brown fox" in str(recognized_text))
        self.assertTrue("jumped over the 5" in str(recognized_text))
        self.assertTrue("lazy dogs!" in str(recognized_text))
        self.assertFalse("And an elephant!" in str(recognized_text))

        file = open(os.path.join(os.path.dirname(__file__), "test_data", "sample1_output.txt"), "r")
        expected_text = file.read()

        self.assertTrue(str(recognized_text) in expected_text)

    def test_read_document_pdf(self):
        locale.setlocale(locale.LC_ALL, 'C')
        recognized_text = read_document(os.path.join(os.path.dirname(__file__),
                                        "test_data", "sample2.pdf"),
                            "eng")['message']

        # print(recognized_text)
        try:
            print("Recognized text is: " + str(recognized_text))
            self.assertTrue("Python Basics" in recognized_text)
            self.assertFalse("Java" in recognized_text)
        except UnicodeEncodeError:
            print("Test has been not passed.")