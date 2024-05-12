# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Movimiento(models.Model):
    _name = 'sa.movimiento'
    _description = 'movimiento'
    _inherit = 'mail.thread'
    
    name = fields.Char(string='Nombre')
    type_move = fields.Selection(selection=[('ingreso','Ingreso'),('gasto','Gasto')],track_visibility="onchange")
    date = fields.Datetime("Fecha")
    amount = fields.Float()
    receip_image = fields.Binary(string='Foto del recibo')
    notas = fields.Html(string="Notas")
    currency_id = fields.Many2one('res.currency')
    id_user =fields.Many2one('res.users',string='Usuario')
    id_category = fields.Many2one('sa.category',string="Categoria")
    tag_ids = fields.Many2many('sa.tag','sa_mov_sa_tag__rel','move_id','tag_id')
class Category(models.Model):
    _name = 'sa.category'
    _description = 'category'
    
    name = fields.Char(string='Nombre')
class Tag(models.Model):
    _name = 'sa.tag'
    _description = 'tag'
    
    name = fields.Char(string='Nombre')
class ResUsers(models.Model):
    _inherit = 'res.users'
    
    ids_movimiento = fields.One2many('sa.movimiento','id_category')
     
