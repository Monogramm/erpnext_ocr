# -*- coding: utf-8 -*-
# Copyright (c) 2021, Monogramm and Contributors
# See license.txt
"""Configuration for desktop."""

from __future__ import unicode_literals

from frappe import _


def get_data():
    """Returns the application desktop icons configuration."""
    return [
        {
            "module_name": "OCR Read",
            "_doctype": "OCR Read",
            "color": "#00bcd4",
            "icon": "fa fa-eye",
            "type": "link",
            "link": "List/OCR Read"
        },

        {
            "module_name": "ERPNext OCR",
            "color": "#00bcd4",
            "icon": "octicon octicon-eye",
            "type": "module",
            "label": _("ERPNext OCR"),
            "hidden": 1
        }
    ]
