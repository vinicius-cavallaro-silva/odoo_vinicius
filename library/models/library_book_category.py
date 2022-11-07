# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class BookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Book Category'
    _parent_store = True

    name = fields.Char(translate=True, required=True)
    # Hierarchy fields
    parent_id = fields.Many2one(
        'library.book.category',
        string='Parent Category',
        ondelete='restrict',
    )
    parent_path = fields.Char(index=True)

    # Optional
    child_ids = fields.One2many(
        'library.book.category',
        'parent_id',
        string='Subcategories',
    )

    highlighted_id = fields.Reference(
        [('library.book', 'Book'),
         ('res.partner', 'Author')],
        'Category Highlight',
    )
