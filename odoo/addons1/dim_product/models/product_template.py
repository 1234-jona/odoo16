# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression

class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_barcode_ids = fields.One2many('product.multi.barcode', 'product_id', 'Multi Barcode')

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = ['|', '|', ('name', operator, name), ('default_code', operator, name),
                  '|', ('product_barcode_ids', operator, name), ('barcode', operator, name)]
        return self._search(expression.AND([domain,args]), limit=limit)

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    trademark_id = fields.Many2one('product.attributes', string='Trademark')
    family_id = fields.Many2one('product.attributes', string='Family')
    product_barcode_ids = fields.One2many('product.multi.barcode', 'product_tmpl_id', string='Multi Barcode')
