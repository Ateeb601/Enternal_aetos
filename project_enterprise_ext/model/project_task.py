from odoo import fields, models
from odoo.exceptions import UserError, ValidationError


class ProjectTask(models.Model):
    _inherit = 'project.task'

    # project_deadline = fields.Datetime(string="Project Deadline")
    # functional_deadline = fields.Datetime(string="Functional Deadline")
    developer_deadline = fields.Datetime(string="Technical Deadline")
    current_status = fields.Char(string="Current Status")
    date_start = fields.Date(
        string="Start Date",
        related='project_id.date_start',
        store=True,
        readonly=False
    )
    date = fields.Date(
        string="End Date",
        related='project_id.date',
        store=True,
        readonly=False
    )
    functional_ids = fields.Many2many(
        'res.users',
        'project_task_functional_rel',  # NEW relation table
        'task_id',
        'user_id',
        string='Functional Assignees',
        tracking = True
    )

    devops_ids = fields.Many2many(
        'res.users',
        'project_task_devops_rel',  # NEW relation table
        'task_id',
        'user_id',
        string='DevOPS Assignees',
        tracking=True
    )

    business_development_ids = fields.Many2many(
        'res.users',
        'project_task_bd_rel',  # NEW relation table
        'task_id',
        'user_id',
        string='Business Development Assignees',
        tracking=True
    )
    web_development_ids = fields.Many2many(
        'res.users',
        'project_task_web_rel',  # NEW relation table
        'task_id',
        'user_id',
        string='Web Development Assignees',
        tracking=True
    )
