# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

from erpnext_ocr.erpnext_ocr.doctype.ocr_language.ocr_language import lang_is_support, check_language_web


class TestOCRLanguage(unittest.TestCase):
    def test_english_language(self):
        decision = lang_is_support("en")
        self.assertTrue(decision)

    def test_check_language_web(self):
        decision = check_language_web("en")
        self.assertEqual(decision, "Yes")
