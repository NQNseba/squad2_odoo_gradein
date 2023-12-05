from odoo import fields, models, api

class GradeInQuestion(models.Model):
    _name = 'gradein.equipment'
    _descrition = 'Grade In Equipment' # con este tag lo identificamos con el views

    name = fields.Char(string='Nombre')
    image = fields.Binary(string='Imagen', attachment=True)
    description = fields.Text(string='Descripción')
    active = fields.Boolean(string='Activo', default=True)
    price = fields.Float(string='Precio')

