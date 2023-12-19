from odoo import fields, models, api

class GradeInAnswer(models.Model):
    _name = 'gradein.answer'
    _description = 'Grade In Answer'

    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active', default=True)
    price_reduction = fields.Float(string='Reduce the price by')
    relacion_id = fields.Many2one('gradein.order', string='relation')