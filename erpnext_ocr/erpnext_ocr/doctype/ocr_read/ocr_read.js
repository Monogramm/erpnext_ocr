// Copyright (c) 2018, John Vincent Fiel and contributors
// For license information, please see license.txt

frappe.ui.form.on('OCR Read', {
	refresh: function(frm) {

	},
	read_image:function (frm) {
		frappe.call({
				method: "read_image",
				doc: cur_frm.doc,
				callback: function (r, rt) {

					if (r.message)
					{
						cur_frm.set_value("read_result",r.message);
					}

				}
			})
	}
});
