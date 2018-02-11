# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_ocr"
app_title = "Erpnext Ocr"
app_publisher = "John Vincent Fiel"
app_description = "OCR"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "johnvincentfiel@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_ocr/css/Aimara.css"
# app_include_js = "/assets/erpnext_ocr/js/Aimara.js"
app_include_css = "/assets/erpnext_ocr/css/treeview.min.css"
app_include_js = "/assets/erpnext_ocr/js/treeview.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_ocr/css/treeview.min.css"
# web_include_js = "/assets/erpnext_ocr/js/treeview.min.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Invoice" : "public/js/Aimara.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_ocr.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_ocr.install.before_install"
# after_install = "erpnext_ocr.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_ocr.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Sales Invoice": {
        # "validate": "chanjeapp.hooks_datadog.SI.validate",
        "on_submit": "erpnext_ocr.zap_hooks.SI.submit",
        # "on_cancel": "chanjeapp.hooks_datadog.SI.amend",
        # "on_trash": "chanjeapp.hooks_datadog.SI.trash"
    },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_ocr.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_ocr.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_ocr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_ocr.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_ocr.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_ocr.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_ocr.event.get_events"
# }

fixtures = ['Custom Script']
