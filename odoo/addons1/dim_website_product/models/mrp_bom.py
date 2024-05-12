from odoo import models,fields,api

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    def action_refresh_data_model(self):
        conector_id = self.env['connector.base'].search([('type_app', '=', 'odoo')])
        line_id = conector_id.connector_model_ids.filtered(lambda m: m.model_id.model==self._name)
        result = line_id._action_read(self)
        vals = result[self.id]['result']
        return vals
        