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

class TestTesseract(unittest.TestCase):
    def test_image_jpg(self):
        im = Image.open(os.path.join(os.path.dirname(__file__), "sample1.jpg"))

        recognized_text = pytesseract.image_to_string(im, lang = 'eng')

        recognized_text.split(" ")

        print(recognized_text)
        self.assertTrue("The quick brown fox" in recognized_text)
        self.assertTrue("jumped over the 5" in recognized_text)
        self.assertTrue("lazy dogs!" in recognized_text)
        self.assertFalse("And an elephant!" in recognized_text)

        file = open(os.path.join(os.path.dirname(__file__), "sample1_output.txt"), "r")
        expected_text = file.read()

        self.assertTrue(recognized_text == expected_text)


    def test_pdf(self):
        pdf = wi(filename = os.path.join(os.path.dirname(__file__), "sample2.pdf"), resolution = 300)
        pdfImage = pdf.convert('jpeg')

        imageBlobs = []

        for img in pdfImage.sequence:
            imgPage = wi(image = img)
            imageBlobs.append(imgPage.make_blob('jpeg'))

        recognized_text = " "

        for imgBlob in imageBlobs:
            im = Image.open(io.BytesIO(imgBlob))
            text = pytesseract.image_to_string(im, lang = 'eng')
            recognized_text = recognized_text + text

        print(recognized_text)
        self.assertTrue("Python Basics" in recognized_text)
        self.assertFalse("Java" in recognized_text)

