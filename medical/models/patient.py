# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

class Patient(models.Model):
    _name = 'medical.patient'
    _description = 'Patient'

    name = fields.Char(string='Nome', required=True)
    age = fields.Integer(string='Idade')
    gender = fields.Selection([('masculino', 'Masculino'),
                               ('feminino', 'Feminino')])
    national_health_card = fields.Char(string='Cartão Nacional de Saúde')
