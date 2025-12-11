from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    ticket_ids = fields.One2many("helpdesk.ticket", "task_id", string="Tickets")
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
            record.todo_ticket_count = len(
                record.ticket_ids.filtered(
                    lambda t: not (t.stage_id and getattr(t.stage_id, 'is_closed', False))
                )
            )
