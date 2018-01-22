import xml.etree.cElementTree as ET

source = '/home/jvfiel/frappe-bl3ndlabs/apps/erpnext_ocr/erpnext_ocr/erpnext_ocr/test.xml'
tree = ET.ElementTree(file=source)
root = tree.getroot()

# for child_of_root in root:
#     print child_of_root.tag, child_of_root.attrib

# for elem in tree.iter():
#     # print elem.tag, elem.attrib
#     # print elem
#     print elem.attrib,elem.tail
#     appt_children = elem.getchildren()
#     # for child in appt_children:
#     #     print elem.attrib, elem.tail

# print root.tag
xmlname = root.tag.split("}")
# print xmlname
xmlname = xmlname[0]
xmlname += "}"
# print xmlname

#Vendor Name
for elem in tree.findall('.//{0}vendor//{0}name//{0}recognizedValue//{0}text'.format(xmlname)):
    print elem.tag, elem.attrib, elem.text
#Vendor Address
for elem in tree.findall('.//{0}vendor//{0}address//{0}text'.format(xmlname)):
    print elem.tag, elem.attrib, elem.text

#Vendor Phone
for elem in tree.findall('.//{0}vendor//{0}phone//{0}recognizedValue//{0}text'.format(xmlname)):
    print elem.tag, elem.attrib, elem.text

# Vendor Phone
for elem in tree.findall('.//{0}vendor//{0}fax//{0}recognizedValue//{0}text'.format(xmlname)):
    print elem.tag, elem.attrib, elem.text

# Vendor PurchaseType
for elem in tree.findall('.//{0}vendor//{0}purchaseType'.format(xmlname)):
    print elem.tag, elem.attrib, elem.text

# Vendor Date
for elem in tree.findall('.//{0}date//{0}text'.format(xmlname)):
    print elem.tag, elem.attrib, elem.text

# # Vendor Time
# for elem in tree.findall('.//{0}time//{0}recognizedValue//{0}text'.format(xmlname)):
#     print elem.tag, elem.attrib, elem.text

# Vendor subTotal
for elem in tree.findall('.//{0}subTotal//{0}text'.format(xmlname)):
    print elem.tag, elem.attrib, elem.text

# # Vendor Total
# for elem in tree.findall('.//{0}total//{0}text'.format(xmlname)):
#     print elem.tag, elem.attrib, elem.text

# Vendor Payment Card Number
for elem in tree.findall('.//{0}payment//{0}cardNumber'.format(xmlname)):
    print elem.tag, elem.attrib, elem.text

# Vendor Payment Value
for elem in tree.findall('.//{0}payment//{0}value//{0}recognizedValue'.format(xmlname)):
    print elem.tag, elem.attrib, elem.text

# Vendor Items
for elem in tree.findall('.//{0}recognizedItems//{0}item'.format(xmlname)):
    # print elem.tag, elem.attrib, elem.text, "*", elem.attrib['index']
    i = elem.attrib['index']
    # for elem in tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}name//{0}text'.format(xmlname,i)):
    #     print elem.tag, elem.attrib, elem.text


    elem = tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}name//{0}text'.format(xmlname, i))[0]
    print elem.tag, elem.attrib, elem.text
    elem = tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}total//{0}recognizedValue//{0}text'.format(xmlname, i))[0]
    print elem.tag, elem.attrib, elem.text
    elem = tree.findall('.//{0}recognizedItems//{0}item[@index="{1}"]//{0}count//{0}normalizedValue'.format(xmlname, i))[0]
    print elem.tag, elem.attrib, elem.text


    # children = elem.getchildren()
    # for child in children:
    #     print elem.tag, elem.attrib, elem.text

# for elem in tree.findall('.//{http://www.abbyy.com/ReceiptCaptureSDK_xml/ReceiptCapture-1.0.xsd}name'):
#     print elem.tag, elem.attrib, elem.text

# appointments = root.getchildren()
# for appointment in appointments:
#     print appointment.attrib
#     appt_children = appointment.getchildren()
#     print "-",appointment.tag
#
#     for appt_child in appt_children:
#         # print "%s=%s" % (appt_child.tag, appt_child.text)
#         print "*",appt_child.attrib,appt_child.tag
#
#         for appt_child_1 in appt_child.getchildren():
#             print "**",appt_child_1.attrib, appt_child_1.tag
#
#             for appt_child_2 in appt_child_1.getchildren():
#
#                 findtext = appt_child_2.text
#
#                 if findtext:
#                     findtext = findtext.strip()
#
#                 if findtext:
#
#                     print "***",appt_child_2.attrib, appt_child_2.tag, appt_child_2.text
#                 else:
#                     for appt_child_3 in appt_child_2.getchildren():
#                         print "***>", appt_child_3.attrib, appt_child_3.tag, appt_child_3.text
#
#
#                     # for apppp in appt_child_1.getchildren():
#             #     print apppp.text
#     # print "-------------------------"
#
# # for attrName, attrValue in root.attributes.items():
# #     #do whatever you'd like
# #     print "attribute %s = %s" % (attrName, attrValue)