# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _

class Patient(models.Model):
    _name = 'medical.patient'
    _inherit = ['res.partner']

    national_health_card = fields.Char(string="Cartão Nacional de Saúde")
    channel_ids = fields.Many2many('mail.channel', 'mail_channel_patient', 'partner_id', 'channel_id')
    visitor_ids = fields.Many2many('website.visitor', 'website_visitor_patient_rel', 'partner_id', 'visitor_id')
