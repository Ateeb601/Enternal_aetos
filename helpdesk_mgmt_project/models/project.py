from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'

    ticket_ids = fields.One2many("helpdesk.ticket", "project_id", string="Tickets")
    ticket_count = fields.Integer(
        compute="_compute_ticket_count", string="Ticket Count"
    )
    todo_ticket_count = fields.Integer(
        string="Number of tickets", compute="_compute_ticket_count"
    )

    @api.depends("ticket_ids", "ticket_ids.stage_id")
    def _compute_ticket_count(self):
        for record in self:
            record.ticket_count = len(record.ticket_ids)
            record.todo_ticket_count = len(record.ticket_ids)
