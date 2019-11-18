frappe.ui.form.on('OCR Read', {
    refresh: function (frm) {

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
            callback: function (r, rt) {
                if (r.message) {
                    console.log(r.message);
                    cur_frm.set_value("read_result", r.message);
                    cur_dialog.hide()
                }
            }
        });
    }
});