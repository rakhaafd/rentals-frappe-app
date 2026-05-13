import frappe

@frappe.whitelist(allow_guest=True)

def get_emoji():
    return "👻"

def throw_emoji(doc, event):
    frappe.throw("This is an error with an emoji! 👻")

def send_payment_reminders():
    pass