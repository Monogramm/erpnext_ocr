# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import os

import frappe
from frappe.model.document import Document


@frappe.whitelist()
def lang_is_supported(lang):
    print(frappe.get_site_path())
    with open(frappe.get_site_path()+"/../../apps/erpnext_ocr/erpnext_ocr/supported_lang.txt", "r") as f:
        for line in f:
            if lang in line:
                return "Yes"
        return "No"


class OCRLanguage(Document):
    pass
