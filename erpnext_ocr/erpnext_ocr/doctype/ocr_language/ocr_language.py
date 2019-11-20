# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
import tesserocr
from frappe.model.document import Document



@frappe.whitelist()
def check_language_web(lang):
    return "Yes" if lang_is_support(lang) else "No"


@frappe.whitelist()
def lang_is_support(lang):
    if lang == 'en':
        lang = "eng"
    list_of_languages = tesserocr.get_languages()[1]
    return lang in list_of_languages


class OCRLanguage(Document):
    pass
