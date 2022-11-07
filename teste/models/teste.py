# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning


class Teste(models.Model):
    _name = 'teste.teste'
    _description = 'Teste'

    name = fields.Char(string='Nome', size=30)
    country = fields.Char(string='Pais', size=30, translate=True)
    true_or_false = fields.Boolean(string="Boolean")
    balance = fields.Float(string='Saldo', digits=(7, 2), translate=True)
    age = fields.Integer(string="Idade")

    option = fields.Selection([('option1', 'Opção 1'), ('option2', 'Opção 2')],
                              string='Action Target', default='option1', required=True)
    note = fields.Text(string='Nota', required=False)
    birthday = fields.Date(string='Data de Nascimento', readonly=True)
    event = fields.Datetime(string='Dia e Horário do Evento', required=True, default=fields.Datetime.now())

    _sql_constraints = [
        ('age', 'CHECK(age > 0 )',
         'The must be major than 0.')
    ]

    @api.onchange('age')
    def age_validator(self):
        for teste in self:
            if teste.age is not None:
                if teste.age >= 0 and teste.age < 18:
                        raise Warning(_('Pessoa menor de idade!'))

    @api.constrains('balance')
    def _check_balance(self):
        for teste in self:
            if teste.balance < 500:
                raise ValidationError(_('Mais probre ainda1'))
            if teste.balance < 1000:
                raise UserError('Pessoa muito pobre!')
