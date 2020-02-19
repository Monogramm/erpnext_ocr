# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import re

import frappe
from erpnext_ocr.erpnext_ocr.doctype.ocr_import_mapping.ocr_import_mapping import find_field, generate_child_doctype
from frappe.model.document import Document


class OCRImport(Document):
    pass


@frappe.whitelist()
def generate_doctype(doctype_import_link, read_result, ignore_mandatory=False, ignore_validate=False):
    """
    generate doctype from raw text
    :param ignore_validate: Ignore validation
    :param ignore_mandatory: Ignore mandatory fields
    :param doctype_import_link:
    :param read_result: text from document
    :return: generated doctype
    """

    doctype_import_doc = frappe.get_doc("OCR Import", doctype_import_link)
    generated_doc = frappe.new_doc(doctype_import_link)

    if ignore_mandatory:
        generated_doc.company = "_Test Company"
        generated_doc.price_list = "_Test Price List"
    generated_doc.flags.ignore_mandatory = ignore_mandatory
    generated_doc.flags.ignore_validate = ignore_validate

    list_with_errors = []
    list_with_table_values = []

    for field in doctype_import_doc.mappings:
        try:
            found_field = find_field(field, read_result)
            if found_field is None:
                frappe.throw(
                    frappe._("Cannot find field {0} in text").format(field.field))
            if field.value_type == "Table":
                iter_of_str = re.finditer(field.regexp, read_result)
                for item_match in iter_of_str:
                    raw_table_doc = generated_doc.append(field.field)
                    raw_table_doc.flags.ignore_mandatory = ignore_mandatory
                    item_str = item_match.group()
                    table_doc = generate_child_doctype(field.link_to_child_doc,
                                                       item_str,
                                                       raw_table_doc)
                    list_with_table_values.append(table_doc)
                    generated_doc.__dict__[field.field] = list_with_table_values
            elif field.value_type == "Date":
                generated_doc.__dict__[field.field] = frappe.utils.get_datetime(found_field)
            else:
                generated_doc.__dict__[field.field] = found_field
        except KeyError:
            list_with_errors.append("Field {} doesn't exist in doctype".
                                    format(doctype_import_doc))
    if list_with_errors:
        frappe.throw(list_with_errors)
    try:
        generated_doc.set_new_name()
        generated_doc.insert()
    except frappe.exceptions.DuplicateEntryError:
        frappe.throw("Generated doc is already exist")
    return generated_doc
