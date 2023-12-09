from odoo import fields, models, api

class GradeInQuestion(models.Model):
    _name = 'gradein.question'
    _description = 'Grade In Question' # con este tag lo identificamos con el views

    name = fields.Char(string="Nombre")
    active = fields.Boolean(default=True, string="Activa")
    equipment_type_ids = fields.Many2many('gradein.equipment', string="Tipo de Equipos")
    answer_ids = fields.Many2many('gradein.answers', string='Respuestas posibles')