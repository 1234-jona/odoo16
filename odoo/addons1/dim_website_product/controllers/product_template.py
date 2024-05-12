# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from re import search

class WebsiteProducts(http.Controller):

    @http.route('/dim_website_product/page1', auth='public', website=True)
    def page1(self,search=None, **kw):
        if search:
            domain = [
            '|', 
            ('default_code', 'ilike', search),
            ('name', 'ilike', search),
        ]
            products = request.env['product.template'].sudo().search(domain)
        else:
            products = request.env['product.template'].search([('website_status', '=', True)])  
        return request.render('dim_website_product.page1', {'products': products,'search_term': search})

    @http.route('/dim_website_product/page2/<int:product_id>', auth='public', website=True)
    def page2(self, product_id, **kw):
        product_id = request.env['product.template'].browse(product_id)
        list_record = {}
        if product_id.id not in list_record:
            list_record[product_id.id] = {
                'domain': [('default_code', '=', product_id.default_code)],
                'vals': {},
                'errores': [],
                'ids': product_id.id_odoo
            }
        vals = product_id.action_refresh_data_model(list_record)
        return request.render('dim_website_product.page2', {'product': product_id, 'list_record': vals})

