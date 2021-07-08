# -*- coding: utf-8 -*-
# Copyright (c) 2021, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import re

import frappe
from frappe.model.document import Document
from frappe.utils import cint


class OCRImportMapping(Document):
    pass


@frappe.whitelist()
def generate_child_doctype(doctype_import_link, string_raw_table_value, table_doc):
    """
    Generate child for some doctype.
    :param doctype_import_link: link to OCR Import
    :param string_raw_table_value: String for future child
    :param doctype_import_doc:
    :param table_doc:
    :return:
    """
    ocr_import_table = frappe.get_doc("OCR Import",
                                      doctype_import_link)
    for table_field in ocr_import_table.mappings:
        found_field = find_field(table_field, string_raw_table_value)
        if found_field is not None:
            table_doc.__dict__[table_field.field] = found_field
            raw_date = table_doc.__dict__[table_field.field]
            if table_field == 'Date':
                table_doc.__dict__[
                    table_field.field] = frappe.utils.get_datetime(raw_date)

    table_doc.parent = ocr_import_table.name
    table_doc.save()

    return table_doc


def find_field(field, read_result):
    """
    :param field: node from mapping
    :param read_result: text from document
    :return: string with value
    """
    pattern_result = None
    if field.regexp:
        pattern_result = re.findall(field.regexp, read_result)

    if field.value_type == "Python":
        found_field = eval(field.value)  # skipcq: PYL-W0123
    else:
        found_field = pattern_result.pop(cint(field.value))

    return found_field
