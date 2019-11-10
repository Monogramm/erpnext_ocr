# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import os

import frappe
from frappe.model.document import Document
from tesserocr import PyTessBaseAPI # For library should download `apt-get install libleptonica-dev libtesseract-dev`

@frappe.whitelist()
def lang_is_supported(lang):
    if lang == 'en':
        lang = "eng"
    with PyTessBaseAPI(path='/usr/share/tesseract-ocr/4.00/tessdata/', lang='eng') as api:
        return "Yes" if lang in api.GetAvailableLanguages() else "No"

class OCRLanguage(Document):
    pass
