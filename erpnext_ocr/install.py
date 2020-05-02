# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe


def before_tests():
    """Frappe trigger before application tests."""
    settings = frappe.get_doc("System Settings")
    settings.time_zone = "Etc/GMT+3"
    settings.language = "en"
    settings.save()
    selling_settings = frappe.get_doc("Selling Settings")
    selling_settings.allow_multiple_items = 1
    selling_settings.save()
