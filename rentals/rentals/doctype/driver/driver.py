# Copyright (c) 2026, rakha and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		first_name: DF.Data | None
		full_name: DF.Data | None
		last_name: DF.Data | None
		phone: DF.Phone | None
	# end: auto-generated types

	def send_alert(self):
		print("alert sent")

	pass
