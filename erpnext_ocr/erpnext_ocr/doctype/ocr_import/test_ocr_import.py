# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt
from __future__ import unicode_literals

import os
import unittest

import frappe
from erpnext_ocr.erpnext_ocr.doctype.ocr_import.ocr_import import generate_doctype


class TestOCRImport(unittest.TestCase):
    def test_generating_doctype(self):
        frappe.set_user("Administrator")
        item_code_mapping = frappe.get_doc(
            {"doctype": "OCR Import Mapping", "field": "item_code", "regexp": "Item Code (\\w+)"})
        item_group_mapping = frappe.get_doc(
            {"doctype": "OCR Import Mapping", "field": "item_group", "regexp": "Item Group (\\w+)"})
        list_with_ocr_import = []
        list_with_ocr_import.append(item_code_mapping)
        list_with_ocr_import.append(item_group_mapping)
        ocr_import = frappe.get_doc(
            {"doctype": "OCR Import", "name": "Item", "mappings": list_with_ocr_import, 'doctype_link': "Item"})
        ocr_read_doctype = frappe.get_doc(
            {"doctype": "OCR Read", "file_to_read": os.path.join(os.path.dirname(__file__),
                                                                 os.path.pardir, os.path.pardir,
                                                                 os.path.pardir,
                                                                 "tests", "test_data",
                                                                 "item.pdf"), "language": "eng"})
        ocr_import.save()
        ocr_read_doctype.ocr_import = ocr_import.name
        ocr_read_doctype.save()
        ocr_read_doctype.read_image()
        generated_item = generate_doctype(ocr_import.name, ocr_read_doctype.read_result)
        self.assertEqual(generated_item.item_code, "fdsa")
        self.assertEqual(generated_item.item_group, "Consumable")
