# -*- coding: utf-8 -*-
# Copyright (c) 2020, Monogramm and Contributors
# See license.txt
"""Configuration for docs."""

from __future__ import unicode_literals


source_link = "https://github.com/Monogramm/erpnext_ocr"
docs_base_url = "https://monogramm.github.io/erpnext_ocr"
headline = "ERPNext OCR Integration"
sub_heading = "Optical Character Recognition using tesseract within ERPNext"


def get_context(context):
    context.brand_html = "ERPNext OCR"
    context.source_link = source_link
    context.docs_base_url = docs_base_url
    context.headline = headline
    context.sub_heading = sub_heading
