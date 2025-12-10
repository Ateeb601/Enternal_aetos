# -*- coding: utf-8 -*-
{
    'name': "Customer Invoice Report",
    'summary': """To print Customer Invoice Report""",
    'description': """To print Customer Invoice Report""",
    'author': "Muhammad Abdullah Nadeem",
    'website': 'linkedin.com/in/abdullah-nadeem-70aa89205/',
    'version': '19.0.0.0.1',
    'depends': ['account'],
    'data': [
        'report/customized_header.xml',
        'report/template.xml',
        'report/report_action.xml',
        'views/account_move.xml',
    ],
    'license': 'LGPL-3',
}
