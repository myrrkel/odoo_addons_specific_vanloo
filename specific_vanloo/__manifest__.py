# -*- coding: utf-8 -*-
# Copyright (C) 2020 - myrrkel (https://github.com/myrrkel).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Specific Vanloo',
    'version': '13.0.0.0',
    'author': 'myrrkel',
    'website': 'https://github.com/myrrkel',
    'summary': "Specific Vanloo customization",
    'sequence': 0,
    'certificate': '',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'sale_management',
        'stock',
        'account',
        'crm',
        'purchase',
        'l10n_fr',
        'product_book',
        'partner_bookshop_import',
        'web_view_google_map',
        'invoice_distributor',
        'mail',
    ],
    'category': 'Specific Modules/Vanloo',
    'complexity': 'easy',
    'description': '''
This module adds specific components for Vanloo Book Publisher.
    ''',
    'qweb': [
    ],
    'demo': [
    ],
    'images': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/report_distributor_order.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
