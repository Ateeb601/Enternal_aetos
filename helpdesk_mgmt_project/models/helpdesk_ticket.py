from odoo import models, fields


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    # task_ids = fields.One2many('project.task', "ticket_id",  string="Project")
    task_count = fields.Integer(string="Tasks Count", compute='_compute_task_count', store=True)
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        help='Project related to this ticket'
    )
    task_id = fields.Many2one(
        'project.task',
        string='Task',
        help='Task linked to this ticket'
    )
    def _compute_task_count(self):
        for ticket in self:
            try:
                ticket.task_count = self.env['project.task'].search_count([('ticket_id', '=', ticket.id)])
            except ValueError:
                # Field ticket_id doesn't exist on project.task yet
                ticket.task_count = 0


    def action_view_task(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tasks',
            'res_model': 'project.task',
            'view_mode': 'kanban,list,form,calendar,pivot,graph,activity',
            'domain': [('ticket_id', '=', self.id)],
            'context': {'default_ticket_id': self.id, 'default_project_id': self.project_id.id, 'default_task_id': self.task_id.id},
        }
