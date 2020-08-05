# **ERPNext OCR** User Guide

This is the User Guide for **ERPNext OCR**.

## Summary
ERPNext OCR provide ability to read documents from images and convert image documents to a Doctype's objects.
Application works on regular expression. It takes necessary text from processed images and generate doctype. 

## Display text from image

1.  Create New `OCR Read` doctype
2.  Choose language and image and save document
3.  After that you can press on `Read file` button and took text from image.

## OCR Import Explanation

`OCR Import` provide create Doctype's objects from image. To fill all information to necessary doctype
`OCR Import` use regular expression.

### Instruction

Create new `OCR Import`
Press on button in 4th column:

![OCR Import](./assets/ocr_import_2.png "OCR Import")

And you will see this window: 

![OCR Import 2](./assets/ocr_import_1.png "OCR Import 2")

| Fields     | Description                                                            |
|------------|------------------------------------------------------------------------|
| Field      | This a name of field in Doctype. For example: `item_code`, `item_name` |
| Regexp     | Regular expression for text in image.                                  |
| Value      | Here you should write `Python Code` or static text                     |
| Value Type | Could be `Table`, `Python`, `Regex Group` or `Date`                    |

*   `Python` - If you choose this type you should write inside `Value` field your python code.

*   `Regex Group` - If you choose this type you should write inside `Regexp`
field your regular expression

*   `Date` - If you choose this type, you should write write inside `Regexp` 
field your regular expression that will find date in document 
( you can configure date format in `System Settings`)

*   `Table` - You should configure another `OCR Import` for tables.

### Example of usage

#### Sales Invoice  Image

![Sales Invoice](./assets/sales_invoice.png "Sales Invoice")

#### OCR Import "Sales Invoice" 

| Field                  | Regexp                                              | Value                                                                                | Value Type | Link To Import Mapping |
|------------------------|-----------------------------------------------------|--------------------------------------------------------------------------------------|------------|------------------------|
| items                  | `.*\W\d+\W([-]?\d+[\.,]\d{2})\W([-]?\d+[\.,]\d{2})` | 0                                                                                    | Table      | Sales Invoice Item     |
| name                   | `qwert`                                             | 0                                                                                    | Python     |                        |
| due_date               | `\d{2}/\d{2}/\d{4}`                                 | 0                                                                                    | Date       |                        |
| against_income_account |                                                     | `frappe.get_doc("Company", frappe.get_all("Company")[0]).default_receivable_account` | Python     |                        |
| party_account_currency |                                                     | `frappe.get_doc("Company", frappe.get_all("Company")[0]).default_currency `          | Python     |                        |
| debit_to               |                                                     | `frappe.get_doc("Company", frappe.get_all("Company")[0]).default_receivable_account` |            |                        |
| conversion_factor      |                                                     | '1'                                                                                  | Python     |                        |

#### OCR Import "Sales Invoice Item"

| Field                  | Regexp             | Value                                                                                                                                                                                                                                                | Value Type  | Link To Import Mapping |
|------------------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|------------------------|
| item_code              | `(\w+.\w)`         | `frappe.get_doc("Item", pattern_result[0]).save().item_code if frappe.db.exists("Item", pattern_result[0]) else frappe.get_doc({"doctype": "Item", "item_code": pattern_result[0],"item_group": "Consumable","stock_uom":"Nos"}).insert().item_code` | Python      |                        |
| item_name              | `(\w+.\w)`         |                                                                                                                                                                                                                                                      | Regex Group |                        |
| rate                   | `[0-9]+`           | '0'                                                                                                                                                                                                                                                  | Regex Group |                        |
|                        |                    |                                                                                                                                                                                                                                                      |             |                        |
| description            |                    | `frappe.get_doc("Item", "SERVICE D").description`                                                                                                                                                                                                    | Python      |                        |
| margin_rate_or_amount  | `[0-9]+\.[0-9]{2}` | '0'                                                                                                                                                                                                                                                  | Regex Group |                        |
| uom                    |                    | `frappe.get_doc("Item", "SERVICE D").uoms[0].uom`                                                                                                                                                                                                    | Python      |                        |
| currency               |                    | `frappe.get_doc("Company", frappe.get_all("Company")[0]).default_currency`                                                                                                                                                                           | Python      |                        |
| amount                 | `[0-9]+\.[0-9]{2}` | '0'                                                                                                                                                                                                                                                  | Regex Group |                        |
| base_rate              | `[0-9]+`           | '0'                                                                                                                                                                                                                                                  | Regex Group |                        |
| income_account         |                    | `frappe.get_doc("Company", frappe.get_all("Company")[0]).default_inventory_account`                                                                                                                                                                  | Python      |                        |
| against_income_account |                    | '0'                                                                                                                                                                                                                                                  | Python      |                        |
| conversion_factor      |                    | '1'                                                                                                                                                                                                                                                  | Python      |                        |
| base_amount            | `[0-9]+\.[0-9]{2}` | 0                                                                                                                                                                                                                                                    | Regexp      |                        |

## License

Copyright © 2020 [Monogramm](https://www.monogramm.io).<br />
This project is **proprietary** licensed.
