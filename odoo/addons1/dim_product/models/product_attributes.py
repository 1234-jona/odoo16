# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductAttributes(models.Model):
    _name = "product.attributes"
    _description = "Custom fields of product attributes"
    _order = 'sequence asc, name'
    
    
    sequence = fields.Integer(string='Sequence', default=10)
    name = fields.Char(string='Description', required=True)
    code = fields.Char(string='Code')
    model_id = fields.Many2one('ir.model', string='Applie to', help="The type of document this template can be used with")
    model = fields.Char('Related Document Model', related='model_id.model', index=True, store=True, required=True)
    model_object_field = fields.Many2one('ir.model.fields', string="Field",
                                         help="Select target field from the related document model.\n"
                                              "If it is a relationship field you will be able to select "
                                              "a target field at the destination of the relationship.")
    res_model = fields.Char('Resource Model', help="The database object this attachment will be attached to.")
    res_id = fields.Integer('Resource ID', help="The record id this is attached to.")
    active = fields.Boolean(string='Active', default=True, help="Set active to false to hide the value without removing it.")
    company_id = fields.Many2one('res.company', string='Company', readonly=True, default=lambda self: self.env.user.company_id)
    option = fields.Char(string='Option Domain', size=50, help='Perform additional criteria filter, in case of using in two forms.')

    _sql_constraints = [
        ('name_uniq', 'unique(name, model_id, model_object_field, company_id)', _('Value already exists')),
    ]
    
    
    @api.model
    def default_get(self, fields):
        res = super(ProductAttributes, self).default_get(fields)
        if self._context.get('field') and self._context.get('default_model'):
            res['model_object_field'] = self.env['ir.model.fields']._get(self._context['default_model'], self._context.get('field')).id
        if self._context.get('default_model'):
            res['model_id'] = self.env['ir.model']._get(self._context.get('default_model')).id
        return res


    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        default.update(
            code=_("%s (copy)") % (self.code or ''),
            name=_("%s (copy)") % (self.name or ''))
        return super(ProductAttributes, self.sudo()).copy(default)

    @api.model
    def create(self, vals):
        if 'name' in vals: vals['name'] = vals['name'].upper()
        if 'model_object_field' not in vals:
            vals['model_object_field'] = self.env['ir.model.fields']._get(self._context['default_model'], self._context.get('field')).id
        if 'model' in vals and 'model_id' not in vals:
            vals['model_id'] = self.env['ir.model']._get(self._context['default_model']).id
        return super(ProductAttributes, self.sudo()).create(vals)

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if operator not in ('ilike', 'like', '=', '=like', '=ilike'):
            return super(ProductAttributes, self).name_search(name, args, operator, limit)
        args = args or []
        domain = [('name', operator, name)]
        recs = self.search(domain + args, limit=limit)
        return recs.name_get()

    def write(self, vals):
        if 'name' in vals: vals['name'] = vals['name'].upper()
        return super(ProductAttributes, self.sudo()).write(vals)
    