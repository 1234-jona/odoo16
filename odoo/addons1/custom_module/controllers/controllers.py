# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class CustomModule(http.Controller):

    @http.route('/custom_module/page1', auth='public', website=True)
    def page1(self, **kw):
        products = request.env['product.template'].search([])
        return request.render('custom_module.page1', {'products': products})

    @http.route('/custom_module/page2/<int:product_id>', auth='public', website=True)
    def page2(self, product_id, **kw):
        product = request.env['product.template'].browse(product_id)
        return request.render('custom_module.page2', {'product': product})