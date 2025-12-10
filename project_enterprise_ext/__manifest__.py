# -*- coding: utf-8 -*-
{
    'name': "Project Task",
    'summary': "Extension in project_task model",
    'author': "Ateeb Shahid Baig",
    'category': 'Project',
    'version': '19.0.1.0',
    'depends': ['project', 'mail', 'hr'],

    'data': [
        'view/project_task_view.xml',
        'view/project_send_message_log_notes.xml',

    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
