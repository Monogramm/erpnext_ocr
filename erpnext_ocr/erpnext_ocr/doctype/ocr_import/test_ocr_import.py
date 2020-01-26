# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and Contributors
# See license.txt
from __future__ import unicode_literals

import unittest

class TestOCRImport(unittest.TestCase):
	pass

	# def test_generating_doctype(self):
	#     frappe.set_user("Administrator")
	#     item_code_mapping = frappe.get_doc(
	#         {"doctype": "OCR Import Mapping", "field": "item_code", "regexp": "Item Code (\\w+)"})
	#     item_group_mapping = frappe.get_doc(
	#         {"doctype": "OCR Import Mapping", "field": "item_group", "regexp": "Item Group (\\w+)"})
	#     list_with_ocr_import = []
	#     list_with_ocr_import.append(item_code_mapping).append(item_group_mapping)
	#     ocr_import = frappe.get_doc({"doctype": "OCR Import", "name": "Item", "mappings": list_with_ocr_import})
	#     ocr_read_doctype = frappe.get_doc(
	#         {"doctype": "OCR Import", "file_to_read": os.path.join(os.path.dirname(__file__),
	#                                                                os.path.pardir, os.path.pardir,
	#                                                                os.path.pardir,
	#                                                                "tests", "test_data",
	#                                                                "item.pdf"), "language": "eng"})