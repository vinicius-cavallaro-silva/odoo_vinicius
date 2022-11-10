# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Member(models.Model):
    _inherit = 'library.member'
    user_id = fields.Many2one('res.users')
