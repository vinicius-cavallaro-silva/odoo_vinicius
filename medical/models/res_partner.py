from odoo import fields, models


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner']

    is_doctor = fields.Boolean(string="É médico?")
    # national_health_card = fields.Char(string='Número do Cartão Nacional de Saúde')
    # cod_cnes = fields.Char(string='Código CNES')
    # is_patient = fields.Boolean(string="Paciente?")


    # accommodation = fields.Char(string='Acomodação')

    # state = fields.Selection([('PR', 'PARANÁ'),
    #                           ('SC', 'SANTA CATARINA'),
    #                           ('RS', 'RIO GRANDE DO SUL'),
    #                           ('SP', 'SÃO PAULO'),
    #                           ('MG', 'MINAS GERAIS'),
    #                           ('RJ', 'RIO DE JANEIRO'),
    #                           ('ES', 'ESPIRITO SANTO'),
    #                           ('MS', 'MATO GROSSO DO SUL'),
    #                           ('MT', 'MATO GROSSO'),
    #                           ('TO', 'TOCANTINS'),
    #                           ('GO', 'GOIÁS'),
    #                           ('DF', 'DISTRITO FEDERAL'),
    #                           ])

    # partner_id = fields.Many2one('res.partner', delegate=True, ondelete='cascade', required=True)

    # hired_cod_provider = fields.Char(string='Cód.Operadora/CNPJ/CPF do Contratado')
    # hired_cod_cnes = fields.Char(string='Código CNES do Contratado')
    #
    #
    # hired_performer_cod_provider = fields.Char(string='Cód.Operadora/CNPJ/CPF do Contratado Executante')
    # hired_performer_name = fields.Char(string='Nome do Contratado Executante')

    #
    #
    #
    # hired_performer_name = fields.Char(string='Nome do Contratado Executante')
    #
    #

    # participation_degree = fields.Selection(
    #     [('Main', 'Principal'),
    #      ('Standard', 'Padrão'),
    #      ('Basic', 'Básico')
    #      ])
    # professional_performer_name = fields.Char(string='Nome do Profissional Executante')
    # professional_board = fields.Char(string='Conselho Profissional')
    # board_number = fields.Integer(string='Número do Conselho')

    # ITIN = fields.Char(string='CPF')

    # request_type = fields.Selection(
    #     [('E', 'Efetiva'),
    #      ('NE', 'Não-Efetiva'),
    #      ])
