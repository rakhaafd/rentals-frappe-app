// Copyright (c) 2026, rakha and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue by Make"] = {
	filters: [
		{
			"fieldname": "my_filter",
			"label": "my_filter",
			"fieldtype": "Link",
			"options": "Vehicle"
		}
	],
};
