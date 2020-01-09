import unittest

from erpnext_ocr.erpnext_ocr.doctype.ocr_read.ocr_read import get_spellchecked_text, get_words_from_text


class MyTestCase(unittest.TestCase):
    def test_spell_checker(self):
        text = get_spellchecked_text("An exampel. I beleive these text is not corect.", "eng")
        self.assertEqual("An example. I believe these text is not correct.", text)

    def test_get_words_from_text(self):
        words = get_words_from_text("Cat in gloves. Catches: no mice.")
        self.assertEqual(["Cat", "in", "gloves", "Catches", "no", "mice"], words)