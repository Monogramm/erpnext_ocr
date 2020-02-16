import frappe


def before_tests():
    settings = frappe.get_doc("System Settings")
    settings.time_zone = "Etc/GMT+3"
    settings.language = "en"
    settings.save()
    selling_settings = frappe.get_doc("Selling Settings")
    selling_settings.allow_multiple_items = 1
    selling_settings.save()