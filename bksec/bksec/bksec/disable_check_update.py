import frappe

@frappe.whitelist()
def remove_update_notification():
    cache = frappe.cache()
    cache.set_value("update-info", "")