# Copyright 2020, Jarsa
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name': 'OpenAcademy',
    'summary': 'Manage trainings',
    'version': '13.0.1.0.0',
    'category': 'School',
    'website': 'https://www.jarsa.com.mx',
    'author': 'Jarsa, Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'depends': [
        'mail',
        'sale_management',
    ],
    'data': [
        'views/openacademy_course_views.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy_session_views.xml',
        'views/res_partner_views.xml',
        'data/res_partner_category_data.xml',
        'views/res_partner_category_views.xml',
        'wizards/openacademy_wizard_view.xml',
        'views/res_users_views.xml',
        'wizards/authorization_wizard_view.xml',
        'reports/openacademy_session_reports.xml',
    ],
    'demo': [
        'demo/openacademy_course_demo.xml',
    ],
}
