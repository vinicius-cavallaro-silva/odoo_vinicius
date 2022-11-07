# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>

{

    'name': 'Library Book Borrowing',
    'version': '13.0.1.0.0',
    'category': 'Pccube',
    'description': 'Members can borrow books from the library.',
    'author': 'Vinicius Cavallaro da Silva, PcCube',
    'website': "https://www.pccube.com",
    'depends': ['library_member'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/checkout_view.xml',
        'data/library_checkout_stage.xml',
        'wizard/checkout_mass_message_wizard.xml',
    ],
}