from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    department_id = fields.Many2one(
        'hr.department',
        compute='_compute_department',
        store=True,
        readonly=True,
    )

    @api.depends('employee_ids.department_id')
    def _compute_department(self):
        for user in self:
            employee = self.env['hr.employee'].search(
                [('user_id', '=', user.id)],
                limit=1
            )
            user.department_id = employee.department_id
