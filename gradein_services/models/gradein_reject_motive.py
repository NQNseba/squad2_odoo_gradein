from odoo import fields, models, api

class GradeInRejectMotive(models.Model):
    _name = 'gradein.reject.motive'
    _description = 'Grade In Reject Motive' # con este tag lo identificamos con el views

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string='Activo', default=True)