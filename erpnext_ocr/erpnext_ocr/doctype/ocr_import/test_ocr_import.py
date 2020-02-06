# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt
from __future__ import unicode_literals

import os
import unittest

import frappe
from erpnext_ocr.erpnext_ocr.doctype.ocr_import.ocr_import import generate_doctype


class TestOCRImport(unittest.TestCase):
    def setUp(self):
        frappe.set_user("Administrator")
        self.item_ocr_read = frappe.get_doc(
            {"doctype": "OCR Read", "file_to_read": os.path.join(os.path.dirname(__file__),
                                                                 os.path.pardir, os.path.pardir,
                                                                 os.path.pardir,
                                                                 "tests", "test_data",
                                                                 "item.pdf"), "language": "eng"})
        self.item_ocr_import = frappe.new_doc("OCR Import")
        self.item_ocr_import.name = "Item"
        self.item_ocr_import.doctype_link = "Item"
        self.item_ocr_import.insert(ignore_permissions=True)
        self.item_ocr_import.save()
        self.item_ocr_read.ocr_import = self.item_ocr_import.name
        self.item_ocr_read.read_image()

        #self.sales_invoice_ocr_import = frappe.new_doc("OCR Import")
        #self.sales_invoice_ocr_import.doctype_link = "Sales Invoice"
        #self.sales_invoice_ocr_import.name = "Sales Invoice"
        #self.sales_invoice_ocr_import.save()

        #self.sales_invoice_ocr_read = frappe.get_doc(
            # {"doctype": "OCR Read", "file_to_read": os.path.join(os.path.dirname(__file__),
            #                                                      os.path.pardir, os.path.pardir,
            #                                                      os.path.pardir,
            #                                                      "tests", "test_data",
            #                                                      "Picture_010.png"), "language": "eng"})

    def tearDown(self):
        self.item_ocr_read.delete()
        self.item_ocr_import.delete()

    def test_generating_item(self):
        item_code_mapping = frappe.get_doc(
            {"doctype": "OCR Import Mapping", "field": "item_code", "regexp": "Item Code (\\w+)",
             "parenttype": "OCR Import", "parent": "Item"})
        item_code_mapping.save(ignore_permissions=True)
        item_group_mapping = frappe.get_doc(
            {"doctype": "OCR Import Mapping", "field": "item_group", "regexp": "Item Group (\\w+)",
             "parenttype": "OCR Import", "parent": "Item"})
        item_group_mapping.save(ignore_permissions=True)
        self.item_ocr_import.append("mappings", item_code_mapping.__dict__)
        self.item_ocr_import.append("mappings", item_group_mapping.__dict__)
        self.item_ocr_import.save()
        generated_item = generate_doctype(self.item_ocr_import.name, self.item_ocr_read.read_result)
        self.assertEqual(generated_item.item_code, "fdsa")
        self.assertEqual(generated_item.item_group, "Consumable")

#    def test_generating_sales_invoice(self):
