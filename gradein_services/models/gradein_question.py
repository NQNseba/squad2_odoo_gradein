from odoo import fields, models, api

class GradeInQuestion(models.Model):
    _name = 'gradein.question'
    _description = 'Grade In Question' # con este tag lo identificamos con el views

    name = fields.Char(string="Name")
    active = fields.Boolean(default=True, string="Active")
    equipment_type_ids = fields.Many2one('gradein.equipment.type', string="Equipment Type")
    answer_ids = fields.Many2many('gradein.answer', string='Answer Given')