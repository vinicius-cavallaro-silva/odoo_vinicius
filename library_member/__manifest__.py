# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
{
    'name': 'Library Members',
    'version': '13.0.1.0.0',
    'category': 'Pccube',
    'author': 'Vinicius Cavallaro da Silva, PcCube',
    'website': "https://www.pccube.com",
    'description': 'Manage people who will be able to borrow books.',
    'depends': ['library', 'mail'],
    "data": [
            'views/book_view.xml',
            'security/library_security.xml',
            'security/ir.model.access.csv',
            'views/member_view.xml',
            'views/library_menu.xml',
            'views/book_list_template.xml',
        ],
    'application': False,
}
