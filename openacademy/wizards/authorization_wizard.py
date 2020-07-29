# Copyright 2020, Jarsa
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models
from odoo.exceptions import ValidationError


class AuthorizationWizard(models.TransientModel):
    _name = 'authorization.wizard'
    _description = "Wizard: Authorization wizard"

    password = fields.Char()

    def authorize(self):
        if self.env.user.authorization_password == self.password:
            sessions = self.env['openacademy.session'].browse(
                self._context.get('active_ids'))
            sessions.write({
                'authorized': True
            })
        else:
            raise ValidationError("The password is incorrect.")
