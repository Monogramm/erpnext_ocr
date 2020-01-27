frappe.ui.form.on('OCR Read', {
    setup: function (frm) {
        frappe.call({
            method: "erpnext_ocr.erpnext_ocr.doctype.ocr_language.ocr_language.get_current_language",
            args: {
                'user': frappe.user['name']
            },
            callback: function (r) {
                cur_frm.set_value("language", r.message);
            }
        })
    },
    read_image: function (frm) {
        frappe.hide_msgprint(true);
        frappe.realtime.on("ocr_progress_bar", function (data) {
            frappe.hide_msgprint(true);
            frappe.show_progress(__("Reading the file"), data.progress[0], data.progress[1]);
        });
        frappe.call({
            method: "read_image",
            doc: cur_frm.doc,
            args: {
                "spell_checker": frm.doc.spell_checker
            },
            callback: function (r) {
                cur_dialog.hide();
                frappe.msgprint(r.message.message);
                cur_frm.refresh();
            }
        });
    },
    import: function (frm) {
        if (typeof frm.doc.ocr_import != "undefined" && frm.doc.ocr_import !== '') {
            frappe.call({
                method: "erpnext_ocr.erpnext_ocr.doctype.ocr_import.ocr_import.generate_doctype",
                args: {
                    "doctype_import_link": frm.doc.ocr_import,
                    "read_result": frm.doc.read_result
                },
                callback: function (r) {
                    console.log(r.message);
                    frappe.show_alert({
                        message: __('Doctype {0} generated',
                            ['<a href="#Form/' + r.message.doctype + '/' + r.message.name + '">' + r.message.name + '</a>']),
                        indicator: 'green'
                    });
                }
            })
        }
        else {
            frappe.throw("Field Template is None");
        }
    }
});
