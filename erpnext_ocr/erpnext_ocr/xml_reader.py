import frappe
from process_xml import recognizeFile

def test_get_xml():
    get_xml("aaa","Picture_010")

def get_xml(docname,filename):
    filename_img = filename+".tif"
    file_url = frappe.get_site_path()+"/private/files/" + filename_img

    filename_xml = filename+".xml"
    file_url_xml = frappe.get_site_path()+"/private/files/" + filename_xml

    recognizeFile(file_url,file_url_xml,"English","xml")

    attachment_doc = frappe.get_doc({
        "doctype": "File",
        "file_name": filename_xml,
        "file_url": "/private/files/" + filename_xml,
        "attached_to_name": docname,
        "attached_to_doctype": "OCR Receipt",
        "old_parent": "Home/Attachments",
        "folder": "Home/Attachments",
        "is_private": 1
    })
    attachment_doc.insert()

    frappe.db.sql("""UPDATE `tabOCR Receipt` SET xml=%s WHERE name=%s""", ("/private/files/" + filename_xml, docname))

    frappe.publish_realtime(event='msgprint',
                            message='Done. Please reload.',
                            user=frappe.session.user)

#bench execute erpnext_ocr.erpnext_ocr.xml_reader.force_attach_file
def force_attach_file():
    filename = "Picture_010.tif"
    name = "aaa"
    force_attach_file_doc(filename,name)

def force_attach_file_doc(filename,name):
    file = "/private/files/"
    # filename = "dimensions.xlsx"
    # name = "bbae02708e"
    # frappe.db.sql("""UPDATE `tabChanje BOM Import` SET attach_file=%s AND name=%s""",(file,name))

    file_url = "/private/files/" + filename

    attachment_doc = frappe.get_doc({
        "doctype": "File",
        "file_name": filename,
        # "file_url": path,
        "file_url": file_url,
        "attached_to_name": name,
        "attached_to_doctype": "OCR Receipt",
        "old_parent": "Home/Attachments",
        "folder": "Home/Attachments",
        "is_private": 1
    })
    attachment_doc.insert()

    frappe.db.sql("""UPDATE `tabOCR Receipt` SET file=%s WHERE name=%s""", (file_url, name))



@frappe.whitelist()
def read(ocr_receipt):
    import xml.etree.cElementTree as ET

    # source = '/home/jvfiel/frappe-bl3ndlabs/apps/erpnext_ocr/erpnext_ocr/erpnext_ocr/test.xml'
    source = frappe.db.sql("""SELECT xml FROM `tabOCR Receipt` WHERE name=%s""", (ocr_receipt))[0][0]
    if source == "" or not source:
        frappe.throw("No XML. Please upload file in OCR again and save to generate.")
    tree = ET.ElementTree(file=frappe.get_site_path()+source)
    root = tree.getroot()

    xmlname = root.tag.split("}")
    # print xmlname
    xmlname = xmlname[0]
    xmlname += "}"
    # print xmlname


    parent_ocr = []

    #Vendor Name
    try:
        vendor_name = tree.findall('.//{0}vendor//{0}name//{0}recognizedValue//{0}text'.format(xmlname))[0].text
        # print elem.tag, elem.attrib, elem.text
    except:
        vendor_name = ""
    parent_ocr.append({"name": "Vendor Name","expanded":True,"children":[{"name": vendor_name}]})
    #Vendor Address
    try:
        vendor_address = tree.findall('.//{0}vendor//{0}address//{0}text'.format(xmlname))[0].text
    except:
        vendor_address = ""
    #    print elem.tag, elem.attrib, elem.text

    parent_ocr.append({"name": "Vendor Address", "expanded": True, "children": [{"name": vendor_address}]})
    #Vendor Phone

    try:
        vendor_phone = tree.findall('.//{0}vendor//{0}phone//{0}recognizedValue//{0}text'.format(xmlname))[0].text
    except:
        vendor_phone = ""

    #    print elem.tag, elem.attrib, elem.text
    parent_ocr.append({"name": "Vendor Phone", "expanded": True, "children": [{"name": vendor_phone}]})
    # Vendor Fax
    # for elem in tree.findall('.//{0}vendor//{0}fax//{0}recognizedValue//{0}text'.format(xmlname)):
    #     print elem.tag, elem.attrib, elem.text

    # Vendor PurchaseType
    try:
        vendor_purchasetype = tree.findall('.//{0}vendor//{0}purchaseType'.format(xmlname))[0].text
    except:
        vendor_purchasetype = ""

    #    print elem.tag, elem.attrib, elem.text
    parent_ocr.append({"name": "Purchase Type", "expanded": True, "children": [{"name": vendor_purchasetype}]})
    # Vendor Date


    try:
        invoice_date = tree.findall('.//{0}date//{0}text'.format(xmlname))[0].text
    except:
        invoice_date = ""


    #    print elem.tag, elem.attrib, elem.text
    parent_ocr.append({"name": "Invoice Date", "expanded": True, "children": [{"name": invoice_date}]})
    # # Vendor Time
    # for elem in tree.findall('.//{0}time//{0}recognizedValue//{0}text'.format(xmlname)):
    #     print elem.tag, elem.attrib, elem.text

    # Vendor subTotal

    try:
        vendor_subTotal = tree.findall('.//{0}subTotal//{0}text'.format(xmlname))[0].text
    except:
        vendor_subTotal = ""


    #    print elem.tag, elem.attrib, elem.text
    parent_ocr.append({"name": "SubTotal", "expanded": True, "children": [{"name": vendor_subTotal}]})
    # # Vendor Total
    # for elem in tree.findall('.//{0}total//{0}text'.format(xmlname)):
    #     print elem.tag, elem.attrib, elem.text

    # Vendor Payment Card Number
    # payment_cardno = tree.findall('.//{0}payment//{0}cardNumber'.format(xmlname))[0].text
    #    print elem.tag, elem.attrib, elem.text

    # Vendor Payment Value
    try:
        payment_val = tree.findall('.//{0}payment//{0}value//{0}recognizedValue//{0}text'.format(xmlname))[0].text
    except:
        payment_val = ""

    #    print elem.tag, elem.attrib, elem.text

    items = []



    # Vendor Items
    parent_item = {"name": 'Recognized Items', "children": []}
    item_children = []
    for elem in tree.findall('.//{0}recognizedItems//{0}item'.format(xmlname)):
        children = []
        parent_item = {"name": 'Item 1', "children": []}
        # child = {"name": 'Sub Item 1', "children": []}

        # print elem.tag, elem.attrib, elem.text, "*", elem.attrib['index']
        i = elem.attrib['index']
        # for elem in tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}name//{0}text'.format(xmlname,i)):
        #     print elem.tag, elem.attrib, elem.text

        #NAME

        try:
            elem = tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}name//{0}text'.format(xmlname, i))[0]
            # print elem.tag, elem.attrib, elem.text
            name = elem.text
        except:
            name = ""

        # name = {"name": elem.text, "children": []}
        parent_item.update({"name":name})



        # children.append(name)
        #TOTAL
        try:
            elem = tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}total//{0}recognizedValue//{0}text'.format(xmlname, i))[0]
            # print elem.tag, elem.attrib, elem.text
            total = elem.text
        except:
            total = ""

        total = {"name": "Amount", "expanded":True,"children": [{"name": total, "children": []}]}
        print total
        children.append(total)
        #COUNT

        try:
            elem = tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}count//{0}normalizedValue'.format(xmlname, i))[0]
            # print elem.tag, elem.attrib, elem.text
            count = elem.text
        except:
            count = ""


        count = {"name": "QTY", "expanded":True,"children": [{"name": count, "children": []}]}
        print count
        children.append(count)

        parent_item.update({"children":children})
        # parent_ocr.update(parent_item)
        item_children.append(parent_item)
    # print items
    parent_ocr.append({"name":"Recognized Items","children":item_children})
    print parent_ocr

    """
        {name: 'Item 1', children: []},
    {name: 'Item 2', expanded: true, children: [
        {name: 'Sub Item 1', children: []},
        {name: 'Sub Item 2', children: []}
    ]
     }

], 'tree'
"""

    # return {
    #     "source":source,
    #     "vendor_name":vendor_name,
    #     "vendor_address":vendor_address,
    #     "vendor_phone":vendor_phone,
    #     "vendor_address":vendor_address,
    #     "invoice_date":invoice_date,
    #     "subTotal":vendor_subTotal,
    #     # "payment_cardno":payment_cardno,
    #     "payment_val":payment_val,
    #     "items":items
    # }
    return parent_ocr

# print read()