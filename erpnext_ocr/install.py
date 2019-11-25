import frappe
from erpnext_ocr.erpnext_ocr.doctype.ocr_language.ocr_language import check_language


def fill_languages():
    all_lang = frappe.get_all("OCR Language")
    for lang in all_lang:
        cur_lang = frappe.get_doc("OCR Language", lang)
        cur_lang.is_supported = check_language(cur_lang.name)
        cur_lang.save()
        print(cur_lang.name + ":" + cur_lang.is_supported)


def after_install():
    fill_languages()