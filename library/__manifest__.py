# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
{
    'name': 'Library',
    'version': '13.0.1.0.0',
    'category': 'Pccube',
    'description': """
            Module made to make some tests
            """,
    'author': 'Vinicius Cavallaro da Silva, PcCube',
    'website': "https://www.pccube.com",
    "depends": ['base'],
    "data": [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml',
        'views/book_category_view.xml',
        'reports/library_book_report.xml',
        'reports/library_book_sql_report.xml',
    ],
    'qweb': [
    ],
    'demo': [
        'data/res.partner.csv',
        'data/library.book.csv',
        'data/book_demo.xml',
     ],
    'installable': True,
    'application': True,
}
