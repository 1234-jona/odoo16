# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    website_status = fields.Boolean(string="Publicar en website")
    id_odoo = fields.Integer(string='ID Odoo External', default=0)
    sync = fields.Boolean(string='Synchronize Registry', help='It will allow registration to be synchronized with the other application.')

    def action_refresh_data_model(self, list_record):
        conector_id = self.env['connector.base'].search([('type_app', '=', 'odoo')])
        line_id = conector_id.connector_model_ids.filtered(lambda m: m.model_id.model==self._name)
        #result = line_id._action_read(list_record)
        values = line_id._action_record_values('get_value_product', list_record)
        #vals = result[self.id]['result']
        #=======================================================================
        # values = {
        #     'product_name': vals['display_name'],
        #     'default_code':vals['default_code'],
        #     'code_type':vals['code_type'][1],
        #     'incoming_qty':vals['incoming_qty'],
        #     'standard_price':vals['standard_price'],
        #     'write_uid':vals['write_uid'][1],
        #     'purchase_requisition':vals['purchase_requisition'],
        #     'product_state_id':vals['product_state_id'],
        #     'type':vals['type'],
        #     'code_type':vals['code_type'][1],
        #     'code_family':vals['code_family'][1],
        #     'presentation_id':vals['presentation_id'],
        #     'barcode_type':vals['barcode_type'],
        #     'barcode':vals['barcode'],
        #     'alternate_code':vals['alternate_code'],
        #     'invoice_policy':vals['invoice_policy'],
        #     'list_price':vals['list_price'],
        #     'standard_price':vals['standard_price'],
        #     'last_purchase':vals['last_purchase'],
        #     'uom_id':vals['uom_id'][1],
        #     'uom_po_id':vals['uom_po_id'][1],
        #     'purchase_method':vals['purchase_method'],
        #     'pe':vals['pe'],
        #     'pme':vals['pme'],
        #     'standard_cost':vals['standard_cost'],
        #     'last_date_revaluation':vals['last_date_revaluation'],
        #     'standard_cost_mod':vals['standard_cost_mod'],
        #     'standard_cost_cif':vals['standard_cost_cif'],
        #     'volume_cd':vals['volume_cd'],
        #     'largo':vals['largo'],
        #     'ancho':vals['ancho'],
        #     'alto':vals['alto'],
        #     'mp_specifications':vals['mp_specifications'],
        #     'mp_tolerance':vals['mp_tolerance'],
        #     'mp_state':vals['mp_state'],
        #     'mp_appearance':vals['mp_appearance'],
        #     'mp_color':vals['mp_color'],
        #     'mp_parameters_c':vals['mp_parameters_c'],
        #     'mp_determination':vals['mp_determination'],
        #     'mp_document':vals['mp_document'],
        #     'label':vals['label'],
        #     'et_material':vals['et_material'],
        #     'et_nso':vals['et_nso'],
        #     'et_image':vals['et_image'],
        #     'ta_image':vals['ta_image'],
        #     'tarr_image':vals['tarr_image'],
        #     'i_sku_stacking':vals['i_sku_stacking'],
        #     'i_sku_by_level':vals['i_sku_by_level'],
        #     'i_sku_per_pallet':vals['i_sku_per_pallet'],
        #     'bale_content':vals['bale_content'],
        #     'package_contents':vals['package_contents'],
        #     'product_duration':vals['product_duration'],
        #     'weight_unit':vals['weight_unit'],
        #     'sleeve_sealing' :vals['sleeve_sealing'],   
        #     'code_trademark':vals['code_trademark'][1],
        #     'bom_count':vals['bom_ids'],
        #     'bom_ids':vals['bom_ids'],
        #     #'bom_line_ids':vals['bom_line_ids']     
        # }
        #=======================================================================
        return values
               
        