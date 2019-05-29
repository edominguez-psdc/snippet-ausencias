# -*- coding: utf-8 -*-
{
    'name': "snippet-ausencias",

    'summary': """
        holi Snippet para el registro de ausencias desde la web.""",

    'description': """
        Modulo que agrega el snippet para el registro de ausencias desde la web y su 
        visualizacion desde el app de ausencias.
    """,

    'author': "PSDC",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Leaves',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_holidays', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'security/hr_holidays_security.xml',
        # 'security/ir.model.access.csv',
        'views/snippet.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}