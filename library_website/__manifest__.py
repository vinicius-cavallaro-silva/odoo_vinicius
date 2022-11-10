# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
{
    'name': 'Library Website',
    'version': '13.0.1.0.0',
    'category': 'Pccube',
    'author': 'Vinicius Cavallaro da Silva, PcCube',
    'website': "https://www.pccube.com",
    'description': 'Create and check book checkout requests.',
    'depends': ['library_checkout', 'website'],
    "data": [
            'security/ir.model.access.csv',
            'security/library_security.xml',
            'views/library_member.xml',
            'views/website_assets.xml',
            'views/helloworld_template.xml',
            'views/checkout_template.xml',
        ],
    'application': False,
}