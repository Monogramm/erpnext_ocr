# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import re
from datetime import datetime

import frappe
from erpnext_ocr.erpnext_ocr.doctype.ocr_import.constants import PYTHON_FORMAT
from frappe.model.document import Document
from frappe.utils import cint


class OCRImport(Document):
    pass


def append_parents_fields(table_doc, field, doctype_to_import):
    table_doc.parentfield = field.field
    table_doc.parenttype = doctype_to_import.name
    table_doc.parent = doctype_to_import.name


@frappe.whitelist()
def generate_child_doctype(doctype_import_link, field, string_raw_table_value, doctype_import_doc, table_doc):
    ocr_import_table = frappe.get_doc("OCR Import",
                                      doctype_import_link)
    for table_field in ocr_import_table.mappings:
        found_field = find_field(table_field, string_raw_table_value)  # table_doc can be here
        if found_field is not None:
            table_doc.__dict__[table_field.field] = found_field
            raw_date = table_doc.__dict__[table_field.field]
            if table_field == 'Date':
                format_from_settings = frappe.get_doc("System Settings").date_format
                table_doc.__dict__[table_field.field] = datetime.strptime(raw_date,
                                                                          PYTHON_FORMAT[format_from_settings])
    append_parents_fields(table_doc, field, doctype_import_doc)
    table_doc.save()
    return table_doc


def find_field(field, read_result):
    if field.value_type == "Python":
        found_field = eval(field.value)  # we can't use ast.literal_eval, because we use strings of code in field.value
    else:
        if field.value_type == "Regex group":
            pattern_result = re.findall(field.regexp, read_result)
        else:
            pattern_result = re.findall(field.regexp, read_result)
        found_field = pattern_result.pop(cint(field.value))
    return found_field


@frappe.whitelist()
def generate_doctype(doctype_import_link, read_result):
    doctype_import_doc = frappe.get_doc("OCR Import", doctype_import_link)
    generated_doc = frappe.new_doc(doctype_import_link)
    list_with_errors = []
    list_with_table_values = []
    for field in doctype_import_doc.mappings:
        try:
            found_field = find_field(field, read_result)  # generated_doc can be send to find_field
            if found_field is not None:
                if field.value_type == "Table":
                    iter = re.finditer(field.regexp, read_result)
                    for item_match in iter:
                        raw_table_doc = generated_doc.append(field.field)
                        item_str = item_match.group()
                        table_doc = generate_child_doctype(field.link_to_child_doc, field, item_str,
                                                           doctype_import_doc,
                                                           raw_table_doc)
                        list_with_table_values.append(table_doc)
                        generated_doc.__dict__[field.field] = list_with_table_values
                elif field.value_type == "Date":
                    format_from_settings = frappe.get_doc("System Settings").date_format
                    generated_doc.__dict__[field.field] = datetime.strptime(found_field,
                                                                            python_format[format_from_settings])
                else:
                    generated_doc.__dict__[field.field] = found_field
            else:
                frappe.throw(frappe._("Cannot find field {0} in text").format(field.field))
        except KeyError:
            list_with_errors.append("Field {} doesn't exist in doctype".format(doctype_import_doc))
    if list_with_errors:
        frappe.throw(list_with_errors)
    try:
        generated_doc.set_new_name()
        generated_doc.insert()
    except frappe.exceptions.DuplicateEntryError:
        frappe.throw("Generated doc is already exist")
    return generated_doc
