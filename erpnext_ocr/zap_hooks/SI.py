import frappe


def validate(doc, method):
    print "datadog"


def trash(doc, method):
    print "datadog"


def amend(doc, method):
    print "datadog"


def submit(doc, method):
    import requests
    r = requests.post("https://hooks.zapier.com/hooks/catch/2929690/ztd17n/", data={'sales_invoice': doc.name, 'customer': doc.customer, 'total': doc.total})
    print "###########################"
    print "###########################"
    print "###########################"
    print "###########################"
    print "###########################"
    print "###########################"
    print(r.status_code, r.reason)
    print(r.text[:300] + '...')