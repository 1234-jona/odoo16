# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductMultiBarcode(models.Model):
    _name = 'product.multi.barcode'
    _description = "Multi Barcode"
    
    name = fields.Char(string='Barcode', required=True)
    type = fields.Selection(selection=[("ean13", "EAN13"), ("ean14", "EAN14")],
        string='Type', required=True, default="ean14")
    product_tmpl_id = fields.Many2one('product.template', string='Product')
    product_id = fields.Many2one('product.product', string='Product Variant')

    _sql_constraints = [('multi_barcode_unique', 'unique(name, type)', 'Barcode Must be different!')]
