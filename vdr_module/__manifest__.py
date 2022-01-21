# -*- coding: utf-8 -*-
{
    'name': "vdr_module",

    'summary': """
        Personalización para VDR
        """,

    'description': """
        Personalización para VDR
    """,

    'author': "Mastermind Software Services",
    'website': "https://mss.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hidden',
    'sequence': 100,
    'version': '0.1',
    'installable': True,
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': ['base','sale','stock','account'],

}
