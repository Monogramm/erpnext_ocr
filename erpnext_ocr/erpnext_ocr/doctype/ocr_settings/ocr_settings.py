# -*- coding: utf-8 -*-
# Copyright (c) 2021, Monogramm and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class OCRSettings(Document):
    def validate(self):
        if not self.pdf_resolution > 0:
            frappe.throw(
                _("PDF Resolution must be a positive integer eg 300 (high) or 200 (normal)."))
