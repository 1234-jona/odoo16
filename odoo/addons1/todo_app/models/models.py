# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TodoApp(models.Model):
    _name = 'todo.app'
    _description = 'Aplicacion que va monstrar las tareas de un usuario'

    name = fields.Char(string='Nombre')
    task = fields.Char(string='Task')

