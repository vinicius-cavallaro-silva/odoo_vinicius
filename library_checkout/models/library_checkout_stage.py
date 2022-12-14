# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CheckoutStage(models.Model):
    _name = 'library.checkout.stage'
    _description = 'Checkout Stage'
    _order = 'sequence,name'

    name = fields.Char(translation=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    fold = fields.Boolean()
    state = fields.Selection(
        [('new', 'New'),
         ('open', 'Borrowed'),
         ('done', 'Returned'),
         ('cancel', 'Cancelled')],
        default='new',
    )
