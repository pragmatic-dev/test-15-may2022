# -*- coding: utf-8 -*-
{
    'name': "Compatibility Themes",

    'summary': """
       This module makes themes modules compatibles between Odoo versions""",

    'description': """
        This module makes themes modules compatibles between Odoo versions.
    """,

    'author': "Pragmatic S.A.S.",
    'website': "https://www.pragmatic.com.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '15.0.0.0.0',
    'license': 'OPL-1',
    'support': 'soporte.fe@pragmatic.com.co',
    'images': ['static/description/icon.jpg'],

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        #'views/assets.xml'
    ],
}
