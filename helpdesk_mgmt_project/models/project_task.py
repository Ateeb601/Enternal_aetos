from odoo import _, api, fields, models

class ProjectTask(models.Model):
    _inherit = "project.task"

    ticket_id = fields.Many2one("helpdesk.ticket", string="Ticket")

    ticket_count = fields.Integer(
        string="Tickets",
        compute="_compute_ticket_count"
    )

    @api.depends('project_id')
    def _compute_ticket_count(self):
        for task in self:
            if task.project_id:
                task.ticket_count = self.env['helpdesk.ticket'].search_count([
                    ('project_id', '=', task.project_id.id)
                ])
            else:
                task.ticket_count = 0


