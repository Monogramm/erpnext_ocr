// Copyright (c) 2018, John Vincent Fiel and contributors
// For license information, please see license.txt

frappe.ui.form.on('OCR Read', {
    refresh: function (frm) {

    },
    read_image: function (frm) {
        frappe.hide_msgprint(true);
        // frappe.realtime.on("ocr_progress_bar", function (data) {
        //     frappe.hide_msgprint(true);
        //     frappe.show_progress(__("Reading the file"), data.progress[0], data.progress[1]);
        //     console.log(data.progress[0])
        // });
        frappe.show_progress(__("Reading the file"), 50, 100);
        frappe.call({
            method: "read_image",
            doc: cur_frm.doc,
            callback: function (r) {
                if (r.message.is_error) {
                    cur_dialog.hide();
                    frappe.msgprint(r.message.message);
                } else {
                    cur_frm.set_value("read_result", r.message);
                }

            }
        });
    }
});