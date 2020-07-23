# Copyright 2020, Jarsa
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class OpenacademySession(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one(
        'res.partner', domain=[
            '|', ('instructor', '=', True),
            ('category_id.name', 'ilike', "Teacher")])
    course_id = fields.Many2one(
        'openacademy.course', ondelete='cascade', required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
