import frappe


def execute(filters=None):
	columns = [
		{
			"fieldname": "make",
			"label": "Make",
			"fieldtype": "Data",
		},
		{
			"fieldname": "total_revenue",
			"label": "Total Revenue",
			"fieldtype": "Currency",
			"options": "IDR",
		},
	]

	data = frappe.db.sql("""
		SELECT
			v.make AS make,
			SUM(rb.total_amount) AS total_revenue
		FROM `tabRide Booking` rb
		LEFT JOIN `tabVehicle` v
			ON rb.vehicle = v.name
		WHERE rb.docstatus = 1
		GROUP BY v.make
		ORDER BY total_revenue DESC
	""", as_dict=True)

	chart = {
		"data": {
				"labels": [x.make for x in data],
				"datasets": [
					{
						"values": [x.total_revenue for x in data],
					}
				],
		},
		"type": "pie"
	}

	return columns, data, "Here is the report", chart