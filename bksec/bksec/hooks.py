# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "bksec"
app_title = "Bksec"
app_publisher = "B & K Securities"
app_description = "Custom DocTypes as required for BKSEC"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "naveen.prabhu@bksec.com"
app_license = "MIT"

fixtures = [ 
		{
			"doctype": "Print Style",
			"filters": {
				"name": [
					"in", ["Modern B & K"]
				]
			}
		},
        "Custom Field", 
        "Client Script", 
        "Property Setter", 
        "Workflow", 
        "Workflow State", 
        "Role", 
        {
            "doctype": "Print Format",
            "filters": {
                "name": ["in", ["TripPrint"]]
                }
        },
        "Workflow Action Master",
        "Workflow State",
        "Workflow",
        "Territory",
        "Warehouse",
        "Location",
        

	]


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bksec/css/bksec.css"
# app_include_js = "/assets/bksec/js/bksec.js"
app_include_js = "/assets/bksec/js/disable_check_update.js"

# include js, css files in header of web template
# web_include_css = "/assets/bksec/css/bksec.css"
# web_include_js = "/assets/bksec/js/bksec.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# meeting_list_js = { "meeting" :"public/js/meeting_list.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "bksec.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bksec.install.before_install"
# after_install = "bksec.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bksec.notifications.get_notification_config"

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
# Jinja Filters
# ---------------
# Methods accessible to print template
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
# 		"bksec.tasks.all"
# 	],
# 	"daily": [
# 		"bksec.tasks.daily"
# 	],
# 	"hourly": [
# 		"bksec.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bksec.tasks.weekly"
# 	]
# 	"monthly": [
# 		"bksec.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "bksec.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bksec.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bksec.task.get_dashboard_data"
# }


