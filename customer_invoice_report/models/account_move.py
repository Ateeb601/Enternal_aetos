from odoo import fields, models, _, api
from odoo.exceptions import UserError, ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    remarks = fields.Text(string = "Remarks")

    def open_customer_invoice_report(self):
        return self.env.ref('customer_invoice_report.customer_invoice_report_action').report_action(self)
