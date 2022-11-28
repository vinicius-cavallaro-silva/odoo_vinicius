# -*- coding: utf-8 -*-
# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
{
    'name': 'Medical',
    'version': '13.0.1.0.0',
    'category': 'Pccube',
    'sequence': '-100',
    'description': """
            Module made to fill medical forms
            """,
    'author': 'Vinicius Cavallaro da Silva, PcCube',
    'website': "https://www.pccube.com",
    "depends": ['base', 'sale'],
    "data": [
        'security/ir.model.access.csv',
        # 'views/surgery_views.xml',
        'views/patient_views.xml',
        # 'views/doctor_views.xml',
        # 'views/configuration_views.xml',
        'views/medical_menu.xml',
    ],
    'application': True,
    'installable': True,
}
