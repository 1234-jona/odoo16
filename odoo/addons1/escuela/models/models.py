# -*- coding: utf-8 -*-

from odoo import fields,api,models

class Profesor(models.Model):
    _name = ('profesor')
    _description = ('Entidad de profesor')
    
    name = fields.Char(string='Nombre del profesor')
    description = fields.Char(string='Descripcion del profesor')
    edad = fields.Integer(string='Edad del profesor')
    state = fields.Boolean(string='Estado del profesor')
    grado = fields.Selection([('primaria','Primaria'),('secundaria','Secundaria')],
                             string='Grado del estudiante', default= 'primaria',
                             required = True)
    profesor_id = fields.Many2one('estudiante')
class Estudiante(models.Model):
    _name = ('estudiante')
    _description = ('Entidad de estudiante')    
    
    name = fields.Char(string='Nombre del estudiante')
    description = fields.Char(string='Descripcion del estudiante')
    edad = fields.Integer(string='Edad del estudiante')
    state = fields.Boolean(string='Estado del estudiante')
    curso = fields.Selection([('primero','Primero'),('segundo','Segundo'),
                              ('tercero','Tercero')],string='Curso del estudiante')
    estudiantes_ids = fields.One2many('profesor','profesor_id')
    