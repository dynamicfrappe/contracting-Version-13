from . import __version__ as app_version

app_name = "contracting_13"
app_title = "Contracting 13"
app_publisher = "dynamic"
app_description = "dynamic"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "beshoy.atef@dynamiceg.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/contracting_13/css/contracting_13.css"
# app_include_js = "/assets/contracting_13/js/contracting_13.js"

# include js, css files in header of web template
# web_include_css = "/assets/contracting_13/css/contracting_13.css"
# web_include_js = "/assets/contracting_13/js/contracting_13.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "contracting_13/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "contracting_13.install.before_install"
# after_install = "contracting_13.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "contracting_13.uninstall.before_uninstall"
# after_uninstall = "contracting_13.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "contracting_13.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"contracting_13.tasks.all"
# 	],
# 	"daily": [
# 		"contracting_13.tasks.daily"
# 	],
# 	"hourly": [
# 		"contracting_13.tasks.hourly"
# 	],
# 	"weekly": [
# 		"contracting_13.tasks.weekly"
# 	]
# 	"monthly": [
# 		"contracting_13.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "contracting_13.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "contracting_13.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "contracting_13.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"contracting_13.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []


override_doctype_class = {
	"Stock Entry": "contracting_13.controllers.custom_stock_entry.customStockEntry" ,
    "Delivery Note": "contracting_13.controllers.custom_delivery_note.CustomDeliveryNote",
	"Sales Invoice": "contracting_13.controllers.custom_sales_invoice.CustomSalesInvoice",
}




doctype_js = {
	"Purchase Order" : "public/js/purchase_order.js" ,
	"Sales Order" : "public/js/sales_order.js" ,
	"Sales Invoice" : "public/js/sales_invoice.js" ,
	"Payment Entry" : "public/js/payment_entry.js" ,
	"Purchase Invoice" : "public/js/purchase_invoice.js" ,
	"Task" : "contracting_13/doctype/task/task.js" ,
	"Stock Entry" : "public/js/stock_entry.js",
	"Quotation" : "public/js/quotation.js",
	"Material Request" :"public/js/material_request.js",

}

domains = {
	'Contracting':'contracting_13.domains.contracting'
}

override_doctype_dashboards = {
	"Project": "contracting_13.public.dashboard.project_get_dashboard_data.get_data"
}

jenv = {
    "methods": [
        "get_comparison_item_cards:contracting_13.contract_api.get_comparison_item_cards",
    ],
    "filters": []
}

scheduler_events = {

	"daily": [
		"contracting_13.contracting_13.doctype.comparison.comparison.get_returnable_insurance"
	],

}

doc_events = {
		"Stock Entry" : {
			"on_submit": "contracting_13.contracting_13.doctype.stock_entry.stock_entry.on_submit"
		} ,
		"Sales Order" : {
			"validate": "contracting_13.contracting_13.doctype.stock_entry.stock_entry.update_project_cost"
		} ,
         "Quotation" : {
			"validate": "contracting_13.controllers.quotation.validate_quotation"
		} ,
		"Purchase Order": {
		"on_submit": "contracting_13.contracting_13.doctype.purchase_order.purchase_order.update_comparison",
		"on_cancel": "contracting_13.contracting_13.doctype.purchase_order.purchase_order.update_comparison",}
}