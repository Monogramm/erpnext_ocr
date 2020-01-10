# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe.model.document import Document

import tesserocr


@frappe.whitelist()
def check_language(lang):
    """Check a language availability. Returns a user friendly text."""
    return frappe._("Yes") if lang_available(lang) else frappe._("No")


@frappe.whitelist()
def lang_available(lang):
    """Call Tesseract OCR to verify language is available."""
    if lang == 'en':
        lang = "eng"
    list_of_languages = tesserocr.get_languages()[1]
    return lang in list_of_languages


@frappe.whitelist()
def get_current_language(user):
    settings = frappe.get_doc("User", user)
    if not settings:
        settings = frappe.get_doc("System Settings")

    lang_code = frappe.get_doc("OCR Language", {"lang": settings.language}).name
    return lang_code if lang_code is not None else "eng"


class OCRLanguage(Document):
    def __init__(self, *args, **kwargs):
        super(OCRLanguage, self).__init__(*args, **kwargs)
        if self.code:
            self.is_supported = check_language(self.code)
