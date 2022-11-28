# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import models, fields

class Doctor(models.Model):
    _name = "medical.physician"
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner','Physician',required=True)
    cod_cnes = fields.Char(string='Código CNES')