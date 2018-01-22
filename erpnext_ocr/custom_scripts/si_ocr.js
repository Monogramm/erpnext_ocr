function copyToClipboard(id) {

    var copyText = document.getElementById(id);
    /* Select the text field */
  copyText.select();

  /* Copy the text inside the text field */
  document.execCommand("Copy");

}


frappe.ui.form.on('Sales Invoice', {
    // validate:function (frm) {
    //
    // },

    refresh: function (frm) {

        cur_frm.add_custom_button(__('OCR'),
            function () {

                var d = new frappe.ui.Dialog({
                    'fields': [
                        {'fieldname': 'ht', 'fieldtype': 'HTML'},
                    ],
                    // primary_action: function(){
                    //     d.hide();
                    //     show_alert(d.get_values());
                    // }
                });


                /*return {
        "source":source,
        "vendor_name":vendor_name,
        "vendor_address":vendor_address,
        "vendor_phone":vendor_phone,
        "vendor_address":vendor_address,
        "invoice_date":invoice_date,
        "subTotal":vendor_subTotal,
        # "payment_cardno":payment_cardno,
        "payment_val":payment_val,
        "items":items
    } */
                 frappe.call({
                     method: "erpnext_ocr.erpnext_ocr.xml_reader.read",
                     // args: {
                     //     "sales_order": cur_frm.doc.sales_order
                     // },
                     callback: function (r, rt) {
                         console.log(r);
                         var html = "";
                         html += "<b>Source: </b><input type='text' id='p1' value='"+r.message['source']+"'><button id='bt1'>Copy Text</button>";
                         html += "<br><b>Vendor Name: </b><input type='text' id='p2' value='"+r.message['vendor_name']+"'><button id='bt2'>Copy Text</button>";
                         html += "<br><b>Vendor Address: </b><input type='text' id='p3' value='"+r.message['vendor_address']+"'><button id='bt3'>Copy Text</button>";
                         html += "<br><b>Invoice Date: </b><input type='text' id='p4' value='"+r.message['invoice_date']+"'><button id='bt4'>Copy Text</button>";
                         html += "<br><b>Sub Total: </b><input type='text' id='p5' value='"+r.message['subTotal']+"'><button id='bt5'>Copy Text</button>";
                         html += "<br><b>Payment Value: </b><input type='text' id='p6' value='"+r.message['payment_val']+"'><button id='bt6'>Copy Text</button>";
                         // html += "<br><b>Vendor Name: </b>"+r.message['vendor_name'];
                         // html += "<br><b>Vendor Address: </b>"+r.message['vendor_address'];
                         // html += "<br><b>Invoice Date: </b>"+r.message['invoice_date'];
                         // html += "<br><b>Sub Total: </b>"+r.message['subTotal'];
                         // html += "<br><b>Payment Value: </b>"+r.message['payment_val'];
                         d.fields_dict.ht.$wrapper.html(html);
                         d.show();
                         document.getElementById("bt1").addEventListener("click", function(){
                           copyToClipboard("p1");
                        }
                        ,false );


                            document.getElementById("bt2").addEventListener("click", function(){
                           copyToClipboard("p2");
                        }
                        ,false );


                            document.getElementById("bt3").addEventListener("click", function(){
                           copyToClipboard("p3");
                        }
                        ,false );


                            document.getElementById("bt4").addEventListener("click", function(){
                           copyToClipboard("p4");
                        }
                        ,false );


                            document.getElementById("bt5").addEventListener("click", function(){
                           copyToClipboard("p5");
                        }
                        ,false );

                            document.getElementById("bt6").addEventListener("click", function(){
                           copyToClipboard("p6");
                        }
                        ,false );


                     }

                 });

            }).addClass("btn-primary")
    }

});