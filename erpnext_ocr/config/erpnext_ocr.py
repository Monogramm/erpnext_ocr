# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
"""Configuration for desktop."""

from __future__ import unicode_literals

from frappe import _


def get_data():
    """Returns the module desktop links configuration."""
    return [
		{
			"label": _("OCR Read"),
			"items": [
				{
					"type": "doctype",
					"name": "OCR Read",
					"description": _("OCR Read"),
				}
				]
		},
		{
			"label": _("OCR Import"),
			"items": [
				{
					"type": "doctype",
					"name": "OCR Import",
					"description": _("OCR Import"),
				}
				]
		}
    ]
