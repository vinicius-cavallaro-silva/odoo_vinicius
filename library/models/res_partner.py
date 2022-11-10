# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    image = fields.Binary(string="Image")
    published_book_ids = fields.One2many(
        'library.book',  # related model
        'publisher_id',  # field for "this" on related model
        string='Published Books')

    book_ids = fields.Many2many(
        'library.book', string='Authored Books')
