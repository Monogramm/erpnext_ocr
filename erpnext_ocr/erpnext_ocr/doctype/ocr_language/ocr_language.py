# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import os

import frappe
import requests
from frappe.model.document import Document

import tesserocr


@frappe.whitelist()
def check_language(lang):
    """Check a language availability. Returns a user friendly text."""
    return frappe._("Yes") if lang_available(lang) else frappe._("No")


@frappe.whitelist()
def lang_available(lang):
    """Call Tesseract OCR to verify language is available."""
    list_of_languages = tesserocr.get_languages()[1]
    if len(lang) == 2:
        return frappe.get_doc("OCR Language", {"lang": lang}).code in list_of_languages

    return lang in list_of_languages


@frappe.whitelist()
def get_current_language(user):
    """Get Tesseract language matching current user or system settings."""
    user = frappe.get_doc("User", user)
    language = user.language
    if not language:
        settings = frappe.get_doc("System Settings")
        language = settings.language

    lang_code = frappe.get_doc("OCR Language", {"lang": language}).name
    return lang_code if lang_code is not None else "eng"


class OCRLanguage(Document):
    def __init__(self, *args, **kwargs):
        super(OCRLanguage, self).__init__(*args, **kwargs)
        if self.code:
            self.is_supported = check_language(self.code)

    def download_tesseract(self):
        if self.type_of_ocr == 'Best':
            res = requests.get(os.getenv('TESSDATA_FAST',
                                         "https://github.com/tesseract-ocr/tessdata_best/blob/master/ara.traineddata?raw"
                                         "=true"))
        elif self.type_of_ocr == 'Fast':
            res = requests.get(os.getenv('TESSDATA_FAST',
                                         "https://github.com/tesseract-ocr/tessdata_fast/blob/master/ara.traineddata?raw"
                                         "=true"))
        elif self.type_of_ocr == 'Custom':
            frappe.throw(frappe._("In progress now. Cannot be imported"))
        with open(
                os.getenv("TESSDATA_PATH", "/usr/share/tesseract-ocr/tessdata/") + self.name + ".traineddata",
                "wb") as file:
            file.write(res.content)
        if os.path.exists(
                os.getenv("TESSDATA_PATH", "/usr/share/tesseract-ocr/tessdata/") + self.name + ".traineddata"):
            self.is_supported = check_language(self.code)
            self.save()
        else:
            frappe.throw(frappe._("File did not download"))