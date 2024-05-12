from odoo import models,fields,api
class ProductTemplate(models.TransientModel):
    _name = 'wizard.product.template'
    date_from = fields.Char()
    date_after = fields.Char()