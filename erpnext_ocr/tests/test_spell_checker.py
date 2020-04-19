# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# For license information, please see license.txt

import unittest

from erpnext_ocr.erpnext_ocr.doctype.ocr_read.ocr_read import get_spellchecked_text, get_words_from_text


class TestSpellChecker(unittest.TestCase):
    def test_spell_checker(self):
        text = get_spellchecked_text("An exampel. I beleive this text is not corect.", "eng")
        self.assertEqual("An example. I believe this text is not correct.", text)

    def test_get_words_from_text(self):
        words = get_words_from_text("Cat in gloves. Catches: no mice.")
        self.assertEqual(["Cat", "in", "gloves", "Catches", "no", "mice"], words)
