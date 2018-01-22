
def read():
    import xml.etree.cElementTree as ET

    source = '/home/jvfiel/frappe-bl3ndlabs/apps/erpnext_ocr/erpnext_ocr/erpnext_ocr/test.xml'
    tree = ET.ElementTree(file=source)
    root = tree.getroot()

    xmlname = root.tag.split("}")
    # print xmlname
    xmlname = xmlname[0]
    xmlname += "}"
    # print xmlname

    #Vendor Name
    vendor_name = tree.findall('.//{0}vendor//{0}name//{0}recognizedValue//{0}text'.format(xmlname))[0].text
        # print elem.tag, elem.attrib, elem.text
    #Vendor Address
    vendor_address = tree.findall('.//{0}vendor//{0}address//{0}text'.format(xmlname))[0].text
    #    print elem.tag, elem.attrib, elem.text

    #Vendor Phone
    vendor_phone = tree.findall('.//{0}vendor//{0}phone//{0}recognizedValue//{0}text'.format(xmlname))[0].text
    #    print elem.tag, elem.attrib, elem.text

    # Vendor Fax
    # for elem in tree.findall('.//{0}vendor//{0}fax//{0}recognizedValue//{0}text'.format(xmlname)):
    #     print elem.tag, elem.attrib, elem.text

    # Vendor PurchaseType
    vendor_purchasetype = tree.findall('.//{0}vendor//{0}purchaseType'.format(xmlname))[0].text
    #    print elem.tag, elem.attrib, elem.text

    # Vendor Date
    invoice_date = tree.findall('.//{0}date//{0}text'.format(xmlname))[0].text
    #    print elem.tag, elem.attrib, elem.text

    # # Vendor Time
    # for elem in tree.findall('.//{0}time//{0}recognizedValue//{0}text'.format(xmlname)):
    #     print elem.tag, elem.attrib, elem.text

    # Vendor subTotal
    vendor_subTotal = tree.findall('.//{0}subTotal//{0}text'.format(xmlname))[0].text
    #    print elem.tag, elem.attrib, elem.text

    # # Vendor Total
    # for elem in tree.findall('.//{0}total//{0}text'.format(xmlname)):
    #     print elem.tag, elem.attrib, elem.text

    # Vendor Payment Card Number
    # payment_cardno = tree.findall('.//{0}payment//{0}cardNumber'.format(xmlname))[0].text
    #    print elem.tag, elem.attrib, elem.text

    # Vendor Payment Value
    payment_val = tree.findall('.//{0}payment//{0}value//{0}recognizedValue//{0}text'.format(xmlname))[0].text
    #    print elem.tag, elem.attrib, elem.text

    items = []

    # Vendor Items
    for elem in tree.findall('.//{0}recognizedItems//{0}item'.format(xmlname)):


        # print elem.tag, elem.attrib, elem.text, "*", elem.attrib['index']
        i = elem.attrib['index']
        # for elem in tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}name//{0}text'.format(xmlname,i)):
        #     print elem.tag, elem.attrib, elem.text

        #NAME
        elem = tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}name//{0}text'.format(xmlname, i))[0]
        # print elem.tag, elem.attrib, elem.text
        name = elem.text
        #TOTAL
        elem = tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}total//{0}recognizedValue//{0}text'.format(xmlname, i))[0]
        # print elem.tag, elem.attrib, elem.text
        total = elem.text
        #COUNT
        elem = tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}count//{0}normalizedValue'.format(xmlname, i))[0]
        # print elem.tag, elem.attrib, elem.text
        count = elem.text
        items.append({"item_code":name,"qty":count,"total":total})

    print items

    return {
        "vendor_name":vendor_name,
        "vendor_address":vendor_address,
        "vendor_phone":vendor_phone,
        "vendor_address":vendor_address,
        "invoice_date":invoice_date,
        "subTotal":vendor_subTotal,
        # "payment_cardno":payment_cardno,
        "payment_val":payment_val,
        "items":items
    }

print read()