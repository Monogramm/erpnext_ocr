// Copyright (c) 2019, Monogramm and contributors
// For license information, please see license.txt

frappe.ui.form.on('OCR Language', "lang", function (frm) {
        if (typeof cur_frm.doc.lang != 'undefined') {
            frappe.call({
                args: {
                    "lang": cur_frm.doc.lang
                },
                method: "erpnext_ocr.erpnext_ocr.doctype.ocr_language.ocr_language.lang_is_supported",
                callback: function (r) {
                    cur_frm.set_value("is_supported", r.message);
                }
            });
        }
    }
);
