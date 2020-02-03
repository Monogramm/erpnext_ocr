# -*- coding: utf-8 -*-
# Copyright (c) 2019, Monogramm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import re
from datetime import datetime

import frappe
from frappe.model.document import Document


class OCRImport(Document):
    pass


def append_parents_fields(table_doc, field, doctype_to_import):
    table_doc.parentfield = field.field
    table_doc.parenttype = doctype_to_import.name
    table_doc.parent = doctype_to_import.name


@frappe.whitelist()
def generate_doctype(doctype_import_link, read_result):
    doctype_import_doc = frappe.get_doc("OCR Import", doctype_import_link)
    generated_doc = frappe.get_doc({"doctype": doctype_import_link})
    list_with_errors = []
    list_with_table_values = []
    for field in doctype_import_doc.mappings:
        try:
            if field.is_not_searchable:
                found_field = field.constant_data
            else:
                found_field = re.search(field.regexp, read_result).group(0)
            if found_field is not None:
                if field.is_table:
                    table_doc = generated_doc.append(field.field)  # table_doc - значение из таблицы
                    ocr_import_table = frappe.get_doc("OCR Import",
                                                      field.link_to_child_doc)  # тут получаем значения детей
                    string = re.findall(field.regexp, read_result).pop(0)
                    for mapped_value in ocr_import_table.mappings:
                        if mapped_value.is_not_searchable:
                            table_doc.__dict__[mapped_value.field] = mapped_value.constant_data
                        else:
                            table_doc.__dict__[mapped_value.field] = re.findall(mapped_value.regexp, string).pop(0)
                    append_parents_fields(table_doc, field, doctype_import_doc)
                    table_doc.save()
                    list_with_table_values.append(table_doc)
                    generated_doc.__dict__[field.field] = list_with_table_values
                    for l in list_with_table_values:
                        l.parent = generated_doc
                else:
                    generated_doc.__dict__[field.field] = found_field
                    if field.is_date:
                        raw_date = generated_doc.__dict__[field.field]
                        print("AAAAAAAAAAAAAAAAA" + raw_date)
                        generated_doc.__dict__[field.field] = datetime.strptime(raw_date,
                                                                                field.format_str)
            else:
                frappe.throw(frappe._("Cannot find field {0} in text").format(field.field))
        except KeyError:
            list_with_errors.append("Field {} doesn't exist in doctype".format(doctype_import_doc))
    if list_with_errors:
        frappe.throw(list_with_errors)
    try:
        generated_doc.save()
    except frappe.exceptions.DuplicateEntryError:
        frappe.throw("Generated doc is already exist")
    return generated_doc
