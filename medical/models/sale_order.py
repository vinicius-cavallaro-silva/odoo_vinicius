# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    participation_degree = fields.Selection(
        [('Main', 'Principal'),
         ('Standard', 'Padrão'),
         ('Basic', 'Básico')
         ])

    # partner_id = fields.Many2one('res.partner', delegate=True, ondelete='cascade', required=True)

    # hired_cod_provider = fields.Char(string='Cód.Operadora/CNPJ/CPF do Contratado')
    # hired_cod_cnes = fields.Char(string='Código CNES do Contratado')
    #
    #
    # hired_performer_cod_provider = fields.Char(string='Cód.Operadora/CNPJ/CPF do Contratado Executante')
    # hired_performer_name = fields.Char(string='Nome do Contratado Executante')
    # hired_cod_cnes = fields.Char(string='Código CNES do Contratado')
    #
    #
    #
    # hired_performer_name = fields.Char(string='Nome do Contratado Executante')
    #
    #


    # professional_performer_name = fields.Char(string='Nome do Profissional Executante')
    # professional_board = fields.Char(string='Conselho Profissional')
    # board_number = fields.Integer(string='Número do Conselho')

    # ITIN = fields.Char(string='CPF')
    # participation_degree = fields.Selection(
    #     [('Main', 'Principal'),
    #      ('Standard', 'Padrão'),
    #      ('Basic', 'Básico')
    #      ])
    # request_type = fields.Selection(
    #     [('E', 'Efetiva'),
    #      ('NE', 'Não-Efetiva'),
    #      ])
