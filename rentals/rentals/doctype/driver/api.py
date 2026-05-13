import frappe

@frappe.whitelist()
def hello():
    return {
        "message": "hello world"
    }