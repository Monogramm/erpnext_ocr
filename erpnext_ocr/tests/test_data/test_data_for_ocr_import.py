test_data_for_sales_invoice = [
    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator', 'modified_by': 'Administrator',
     'parent': 'Sales Invoice', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'name',
     'value': '0', 'value_type': 'Python'
     },
    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice',
     'parenttype': 'OCR Import',

     'link_to_child_doc': 'Sales Invoice Item', 'field': 'items',

     'regexp': '.*\\W\\d+\\W([-]?\\d+[\\.,]\\d{2})\\W([-]?\\d+[\\.,]\\d{2})', 'value': '0',

     'value_type': 'Table'},

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice',
     'parenttype': 'OCR Import',

     'link_to_child_doc': None, 'field': 'due_date',

     'regexp': '\\d{2}\\/\\d{2}/\\d{4}', 'value': '0',

     'value_type': 'Date'},

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'modified_by': 'Administrator', 'parent': 'Sales Invoice',
     'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'against_income_account',
     'regexp': '',
     'value': 'frappe.get_doc("Company", "fsda").default_bank_account',

     'value_type': 'Python', },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'modified_by': 'Administrator', 'parent': 'Sales Invoice',
     'parenttype': 'OCR Import',

     'link_to_child_doc': None, 'field': 'party_account_currency',

     'regexp': None, 'value': 'frappe.get_doc("Company", "fsda").default_currency',

     'value_type': 'Python', },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'modified_by': 'Administrator', 'parent': 'Sales Invoice',
     'parenttype': 'OCR Import',

     'link_to_child_doc': None, 'field': 'debit_to',
     'regexp': None, 'value': '"Debtors - F"',

     'value_type': 'Python', }]
test_data_for_sales_invoice_items = [
    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator', 'modified_by': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'item_code',
     'regexp': '(SERVICE D \\D+)', 'value': '0',
     'value_type': 'Regex group', },
    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'item_name',
     'regexp': '(SERVICE D \\D+)', 'value': '0',
     'value_type': 'Regex group'},

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'qty',
     'regexp': '1', 'value': '0',
     'value_type': 'Regex group', },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'rate',
     'regexp': '[0-9]+', 'value': '0',

     'value_type': 'Regex group', },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'description',
     'regexp': '', 'value': 'frappe.get_doc("Item", "SERVICE D").description',
     'value_type': 'Python',
     },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'margin_rate_or_amount',

     'regexp': '[0-9]+\\.[0-9]{2}', 'value': '0',
     'value_type': 'Regex group', },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',

     'link_to_child_doc': None, 'field': 'uom',
     'regexp': None,
     'value': 'frappe.get_doc("Item", "SERVICE D").uoms[0].uom',
     'value_type': 'Python',
     },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',

     'link_to_child_doc': None, 'field': 'currency',
     'regexp': None,
     'value': 'frappe.get_doc("Company",{\'name\': \'fsda\'}).default_currency',
     'value_type': 'Python', },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',

     'link_to_child_doc': None, 'field': 'amount',
     'regexp': '[0-9]+\\.[0-9]{2}', 'value': '0',
     'value_type': 'Regex group', },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'base_rate',
     'regexp': '[0-9]+', 'value': '0',

     'value_type': None, },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'income_account',
     'regexp': None, 'value': "'Sales - F'",
     'value_type': 'Python', },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'against_income_account',
     'regexp': None, 'value': "'0'",
     'value_type': 'Python', },

    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'base_amount',
     'regexp': '[0-9]+\\.[0-9]{2}', 'value': '0',
     'value_type': 'Regex group', },
    {'doctype': 'OCR Import Mapping',
     'owner': 'Administrator',
     'parent': 'Sales Invoice Item', 'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'conversion_factor',

     'regexp': None, 'value': "'1'",

     'value_type': 'Python', },
    {'doctype': 'OCR Import Mapping', 'owner': 'Administrator', 'parent': 'Sales Invoice Item',
     'parenttype': 'OCR Import',
     'link_to_child_doc': None, 'field': 'base_rounded_total', 'value': "'123'", 'value_type': 'Python'}
]
