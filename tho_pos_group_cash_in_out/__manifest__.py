# -*- coding: utf-8 -*-
{
    'name': "POS Group cash in/out",

    'summary': """
        Type of grouping for the Cash in/out""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Thomas Edward",
    'website': "https://thomasedward.website/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        'security/groups.xml',
        # 'security/ir.model.access.csv',
        # 'views/asset.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'tho_pos_group_cash_in_out/static/src/js/cash_in_out.js',
        ],
    },
    'price': 10.0,
    'currency': "EUR",
    'images': ['static/description/banner.gif'],
    'application': True,
}
