# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt
from __future__ import unicode_literals

import os
import unittest

import frappe
from erpnext_ocr.erpnext_ocr.doctype.ocr_import.ocr_import import generate_doctype
from erpnext_ocr.tests.test_data.test_data_for_ocr_import import test_data_for_sales_invoice_items, \
    test_data_for_sales_invoice


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

        self.sales_invoice_ocr_import = frappe.new_doc("OCR Import")
        self.sales_invoice_ocr_import.doctype_link = "Sales Invoice"
        self.sales_invoice_ocr_import.name = "Sales Invoice"
        self.sales_invoice_ocr_import.save()

        self.sales_invoice_ocr_read = frappe.get_doc(
            {"doctype": "OCR Read", "file_to_read": os.path.join(os.path.dirname(__file__),
                                                                 os.path.pardir, os.path.pardir,
                                                                 os.path.pardir,
                                                                 "tests", "test_data",
                                                                 "Picture_010.png"), "language": "eng"})
        self.sales_invoice_ocr_read.read_image()

    def tearDown(self):
        self.item_ocr_read.delete()
        self.item_ocr_import.delete()
        self.sales_invoice_ocr_read.delete()
        self.sales_invoice_ocr_import.delete()
        if frappe.db.exists("OCR Import", "Sales Invoice Item"):
            frappe.get_doc("OCR Import", "Sales Invoice Item").delete()


    def test_generating_item(self):
        item_code_mapping = frappe.get_doc(
            {"doctype": "OCR Import Mapping", "field": "item_code", "regexp": "Item Code (\\w+)",
             "parenttype": "OCR Import", "value_type": "Regex group", "parent": "Item"})
        item_code_mapping.save(ignore_permissions=True)
        item_group_mapping = frappe.get_doc(
            {"doctype": "OCR Import Mapping", "value_type": "Regex group", "field": "item_group",
             "regexp": "Item Group (\\w+)",
             "parenttype": "OCR Import", "parent": "Item"})
        item_group_mapping.save(ignore_permissions=True)
        self.item_ocr_import.append("mappings", item_code_mapping.__dict__)
        self.item_ocr_import.append("mappings", item_group_mapping.__dict__)
        self.item_ocr_import.save()
        generated_item = generate_doctype(self.item_ocr_import.name, self.item_ocr_read.read_result)
        self.assertEqual(generated_item.item_code, "fdsa")
        self.assertEqual(generated_item.item_group, "Consumable")
        generated_item.delete()

    def test_generating_sales_invoice(self):
        sales_invoice_template = frappe.new_doc("OCR Import")
        sales_invoice_template.doctype_link = "Sales Invoice"
        create_items(sales_invoice_template)
        for dict_with_data in test_data_for_sales_invoice:
            ocr_import_mapping = frappe.get_doc(dict_with_data)
            if ocr_import_mapping.value_type == "Table":
                ocr_import_mapping.link_to_child_doc = "Sales Invoice Item"
            ocr_import_mapping.save()
        self.sales_invoice = generate_doctype("Sales Invoice", self.sales_invoice_ocr_read.read_result)

def create_items(sales_invoice_template):
    sales_invoice_item_template = frappe.new_doc("OCR Import")
    sales_invoice_item_template.doctype_link = "Sales Invoice Item"
    mappings = []
    for dict_with_data in test_data_for_sales_invoice_items:
        item = frappe.get_doc(dict_with_data)
        item.parent = sales_invoice_template
        mappings.append(item)
    sales_invoice_item_template.mappings = mappings
    sales_invoice_item_template.save()
    return sales_invoice_item_template
