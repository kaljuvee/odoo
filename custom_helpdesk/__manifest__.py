{
    'name': 'Custom Helpdesk',
    'version': '17.0.1.0.0',
    'category': 'Services',
    'summary': 'Simple Helpdesk Ticket Management System',
    'description': """
Custom Helpdesk Module
======================

A simple helpdesk ticket management system built with Odoo Community Edition.

Features:
---------
* Create and manage support tickets
* Assign tickets to team members
* Track ticket status and priority
* Customer portal access
* Email notifications
* Reporting and analytics

This module provides basic helpdesk functionality using Odoo Community features.
    """,
    'author': 'Custom Development',
    'website': 'https://github.com/kaljuvee/odoo',
    'depends': ['base', 'mail', 'portal', 'web'],
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'data/helpdesk_data.xml',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_team_views.xml',
        'views/helpdesk_menus.xml',
        'views/portal_templates.xml',
    ],
    'demo': [
        'data/helpdesk_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
