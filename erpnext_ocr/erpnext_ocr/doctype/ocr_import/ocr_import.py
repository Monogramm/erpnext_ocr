# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import re

import frappe
from frappe.model.document import Document

class OCRImport(Document):
	pass

@frappe.whitelist()
def generate_doctype(doctype_import_link, read_result):
	doctype_import_doc = frappe.get_doc("OCR Import", doctype_import_link)
	generated_doc = frappe.get_doc({"doctype": doctype_import_link})
	list_with_errors = []
	for field in doctype_import_doc.mappings:
		try:
			found_field = re.search(field.regexp, read_result)
			if found_field is not None:
				generated_doc.__dict__[field.field] = re.findall(field.regexp, read_result).pop(0)
			else:
				frappe.throw(frappe._("Cannot find field {0} in text").format(field.field))
		except KeyError:
			list_with_errors.append("Field {} doesn't exist in doctype".format(doctype_import_doc))
	if list_with_errors:
		frappe.throw(list_with_errors)
	generated_doc.save()
	return generated_doc