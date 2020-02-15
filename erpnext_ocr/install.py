import frappe


def before_tests():
    settings = frappe.get_doc("System Settings")
    settings.time_zone = "Etc/GMT+3"
    settings.language = "en"
    settings.save()