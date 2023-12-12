from odoo import fields, models

class GradeInEquipmentType(models.Model):
    _name = 'gradein.equipment.type'
    _description = 'Grade In Equipment Type'

    name = fields.Char(string='Nombre')
    image = fields.Binary(string='Imagen', attachment=True)
    active = fields.Boolean(string='Activo', default=True)
    question_ids = fields.One2many('gradein.question', 'equipment_type_ids', string='Preguntas')