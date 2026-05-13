# Copyright (c) 2026, rakha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from rentals.rentals.doctype.ride_booking_item.ride_booking_item import RideBookingItem

		amended_from: DF.Link | None
		driver: DF.Link
		items: DF.Table[RideBookingItem]
		order: DF.Link
		rate: DF.Currency
		total_amount: DF.Currency
		vehicle: DF.Link | None
	# end: auto-generated types

	def validate(self):
		
		if not self.rate:
			self.rate = frappe.db.get_single_value("Rentals Settings", "standard_rate")

		total_distance = 0
		for item in self.items:
			total_distance += item.distance

		self.total_amount = total_distance * self.rate
