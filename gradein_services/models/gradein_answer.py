from odoo import fields, models

class GradeInAnswer(models.Model):
    _name = 'gradein.answer'
    _description = 'Grade In Answer'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string='Activa', default=True)
    price_reduction = fields.Float(string='Reduce el precio en')
    relacion_id = fields.Many2one('gradein.order', string='relacion')