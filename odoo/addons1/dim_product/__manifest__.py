# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Product',
    'version': '1.0',
    'summary': 'Manage your stock and logistics activities',
    'website': 'https://www.odoo.com/app/inventory',
    'depends': [
        # Odoo
        'product',
        
        # Odoo Community
    ],
    'category': 'Inventory/Inventory',
    'author': 'Jefferson Tipan',
    'sequence': 26,
    'demo': [],
    'data': [
        # Data
        #'data/stock_picking_data.xml',
        
        # Security
        #'security/stock_security.xml',
        'security/ir.model.access.csv',
        
        # Views
        'views/product_attributes_views.xml',
        'views/product_template_views.xml',
        
        # Wizard
        #'wizard/stock_pick_wizard_views.xml',
    ],
    'installable': True,
    'application': True,
    'pre_init_hook': False,
    'post_init_hook': False,
    'license': 'GPL-3',
    'assets': {
        'web.assets_backend': [],
    }
}
