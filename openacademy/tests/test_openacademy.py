# Copyright 2020, Jarsa
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestOpenacademy(TransactionCase):

    def setUp(self):
        super().setUp()
        self.course = self.env.ref('openacademy.course0')

    def test_10_openacademy(self):
        session = self.env['openacademy.session'].create({
            'name': 'Test',
            'course_id': self.course.id,
        })
        self.assertEqual(session.state, 'draft')
        session.action_confirm()
        self.assertEqual(session.state, 'confirmed')
