from odoo import fields, models, api

class GradeInEquipment(models.Model):
    _name = 'gradein.equipment'
    _description = 'Grade In Equipment' # con este tag lo identificamos con el views

    name = fields.Char(string='Name')
    image = fields.Image(string='Image', attachment=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    price = fields.Float(string='Price')

