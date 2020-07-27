# Copyright 2020, Jarsa
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean()
    session_ids = fields.Many2many(
        'openacademy.session', string="Attended Sessions", readonly=True)
    course_ids = fields.Many2many(
        'openacademy.course', string="Courses")
