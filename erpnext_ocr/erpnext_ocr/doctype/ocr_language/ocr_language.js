// Copyright (c) 2019, Monogramm and contributors
// For license information, please see license.txt

frappe.ui.form.on('OCR Language',
    {
        download: function (frm) {
            frappe.call({
                method: "download_tesseract",
                doc: frm.doc,
                success: function (r) {
                    cur_frm.set_value("is_supported", "Yes");
                }
            })
        }
    });
