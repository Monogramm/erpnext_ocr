function copyToClipboard(id) {
    console.log(id);
    console.log(id);
    console.log(id);
    var copyText = document.getElementById(id);
    /* Select the text field */
  copyText.select();

  /* Copy the text inside the text field */
  document.execCommand("Copy");

}

frappe.ui.form.on('Sales Invoice', 'ocr_receipt',
    function(frm){

    console.log('OCR RECEIPT');

    });


frappe.ui.form.on('Sales Invoice', {
    // validate:function (frm) {
    //
    // },

    refresh: function (frm) {

        cur_frm.add_custom_button(__('OCR'),
            function () {


                if (cur_frm.doc.ocr_receipt) {
                    var d = new frappe.ui.Dialog({
                        'fields': [
                            // {'fieldname': 'ocr_receipt', 'fieldtype': 'Link','options':'OCR Receipt', 'label': 'OCR Receipt', 'reqd': 1} ,
                            {'fieldname': 'ht', 'fieldtype': 'HTML'},
                        ],
                        // primary_action: function(){
                        //     d.hide();
                        //     show_alert(d.get_values());
                        // }
                    });

                    frappe.call({
                        method: "erpnext_ocr.erpnext_ocr.xml_reader.read",
                        args: {
                            "ocr_receipt": cur_frm.doc.ocr_receipt
                        },
                        callback: function (r, rt) {
                            console.log(r);
                            var html = "";
                            html += "<div class='row'><div class='col-xs-2'>" +
                                "<b>Source: </b></div><div class='col-xs-5'>" +
                                "<input type='text' id='p1' value='" + r.message['source'] + "' class='form-check-input'></div>" +
                                "<div class='col-xs-3'><button id='bt1' class='btn btn-primary'>Copy Text</button></div></div>";


                            html += "<br><div class='row'> <div class='col-xs-2'><b>Vendor Name: </b></div>" +
                                "<div class='col-xs-5'> <input type='text' id='p2' value='" + r.message['vendor_name'] + "' class='form-check-input'></div>" +
                                "<div class='col-xs-3'> <button id='bt2' class='btn btn-primary'>Copy Text</button></div></div>";


                            // html += "<br><b>Vendor Address: </b><input type='text' id='p3' value='" + r.message['vendor_address'] + "'><button id='bt3'>Copy Text</button>";
                            // html += "<br><b>Invoice Date: </b><input type='text' id='p4' value='" + r.message['invoice_date'] + "'><button id='bt4'>Copy Text</button>";
                            // html += "<br><b>Sub Total: </b><input type='text' id='p5' value='" + r.message['subTotal'] + "'><button id='bt5'>Copy Text</button>";
                            // html += "<br><b>Payment Value: </b><input type='text' id='p6' value='" + r.message['payment_val'] + "'><button id='bt6'>Copy Text</button>";

                              html += "<br><div class='row'> <div class='col-xs-2'><b>Vendor Address: </b></div>" +
                                "<div class='col-xs-5'> <input type='text' id='p3' value='" + r.message['vendor_address'] + "' class='form-check-input'></div>" +
                                "<div class='col-xs-3'> <button id='bt3' class='btn btn-primary'>Copy Text</button></div></div>";

                             html += "<br><div class='row'> <div class='col-xs-2'><b>Invoice Date: </b></div>" +
                                "<div class='col-xs-5'> <input type='text' id='p4' value='" + r.message['invoice_date'] + "' class='form-check-input'></div>" +
                                "<div class='col-xs-3'> <button id='bt4' class='btn btn-primary'>Copy Text</button></div></div>";

                                      html += "<br><div class='row'> <div class='col-xs-2'><b>Sub Total: </b></div>" +
                                "<div class='col-xs-5'> <input type='text' id='p5' value='" + r.message['subTotal'] + "' class='form-check-input'></div>" +
                                "<div class='col-xs-3'> <button id='bt5' class='btn btn-primary'>Copy Text</button></div></div>";

                                 html += "<br><div class='row'> <div class='col-xs-2'><b>Payment Value: </b></div>" +
                                "<div class='col-xs-5'> <input type='text' id='p6' value='" + r.message['payment_val'] + "' class='form-check-input'></div>" +
                                "<div class='col-xs-3'> <button id='bt6' class='btn btn-primary'>Copy Text</button></div></div>";

                            html += "<br><br><b>Recognized Items: </b>";
                            //ITEMS
                            for (var i = 0; i < r.message['items'].length; i++) {
                                console.log(i);
                                // html += "<br><b>Item Name: </b><input type='text' id='p7_" + i + "' value='" + r.message['items'][i]['item_code'] + "'><button id='bt7_" + i + "'>Copy Text</button>";
                                // html += "<br><b>Qty.: </b><input type='text' id='p7_" + i + "' value='" + r.message['items'][i]['qty'] + "'><button id='bt7_" + i + "'>Copy Text</button>";
                                // html += "<br><b>Amount: </b><input type='text' id='p7_" + i + "' value='" + r.message['items'][i]['total'] + "'><button id='bt7_" + i + "'>Copy Text</button><br>";


                                 html += "<br><div class='row'> <div class='col-xs-2'><b>Name: </b></div>" +
                                "<div class='col-xs-5'> " +
                                     "<input type='text' id='p7_" + (i).toString() + "' value='" + r.message['items'][i]['item_code'] + "' class='form-check-input'></div>" +
                                "<div class='col-xs-3'> <button id='bt7_" + (i).toString() +"' class='btn btn-primary'>Copy Text</button></div></div>";

                                 html += "<div class='row'> <div class='col-xs-2'><b>Qty.: </b></div>" +
                                "<div class='col-xs-5'> " +
                                     "<input type='text' id='p8_" + (i).toString() + "' value='" + r.message['items'][i]['qty'] + "' class='form-check-input'></div>" +
                                "<div class='col-xs-3'> <button id='bt8_" + (i).toString() +"' class='btn btn-primary'>Copy Text</button></div></div>";

                                 html += "<div class='row'> <div class='col-xs-2'><b>Amount: </b></div>" +
                                "<div class='col-xs-5'> " +
                                     "<input type='text' id='p9_" + (i).toString() + "' value='" + r.message['items'][i]['total'] + "' class='form-check-input'></div>" +
                                "<div class='col-xs-3'> <button id='bt9_" + (i).toString() +"' class='btn btn-primary'>Copy Text</button></div></div>";


                            }
                            console.log(html);

                            d.fields_dict.ht.$wrapper.html(html);
                            d.show();
                            document.getElementById("bt1").addEventListener("click", function () {
                                    copyToClipboard("p1");
                                }
                                , false);


                            document.getElementById("bt2").addEventListener("click", function () {
                                    copyToClipboard("p2");
                                }
                                , false);


                            document.getElementById("bt3").addEventListener("click", function () {
                                    copyToClipboard("p3");
                                }
                                , false);


                            document.getElementById("bt4").addEventListener("click", function () {
                                    copyToClipboard("p4");
                                }
                                , false);


                            document.getElementById("bt5").addEventListener("click", function () {
                                    copyToClipboard("p5");
                                }
                                , false);

                            document.getElementById("bt6").addEventListener("click", function () {
                                    copyToClipboard("p6");
                                }
                                , false);

                            var ii, bb, pp;
                            for (ii = 0; ii < r.message['items'].length; ii++) {
                                (function () {
                                    console.log(ii);
                                    var j = ii;
                                    var bb = "bt7_" + (j).toString();
                                    var pp = "p7_" + (j).toString();
                                    console.log(bb);
                                    console.log(pp);

                                    document.getElementById(bb).addEventListener("click", function () {
                                            copyToClipboard(pp);
                                        }
                                        , false);

                                    document.getElementById("bt8_" + (j).toString()).addEventListener("click", function () {
                                            copyToClipboard("p8_" + (j).toString());
                                        }
                                        , false);

                                    document.getElementById("bt9_" + (j).toString()).addEventListener("click", function () {
                                            copyToClipboard("p9_" + (j).toString());
                                        }
                                        , false);
                               }());
                            }

                            // document.getElementById('bt7_0').addEventListener("click", function () {
                            //             copyToClipboard('p7_0');
                            //         }
                            //         , false);



                        }

                    });
                }
                else
                {
                    frappe.msgprint("Please select OCR Receipt first.");
                }

            }).addClass("btn-primary")

    }

});