from odoo import models, fields

class GradeInOrder(models.Model):
    _name = "gradein.order"
    _description = "Grade in Order"

    name = fields.Char(string="Nombre")
    date = fields.Date(string="Fecha")
    state = fields.Selection([
        ('draft','borrador'),
        ('confirmed','confirmado'),
        ('rejected','rechazado'),], string='Estado', default='draft')
    equipment_id = fields.Many2one('gradein.equipment', string='Equipo')
    imei = fields.Integer(string='IMEI')
    image_ids = fields.Many2many('ir.attachment',domain="[('res_model', '=', 'gradein.equipment')]", string='Imagen')
    partner_id = fields.Many2one('res.partner', string='Cliente')
    ##reject_motive_id = fields.Many2one('gradein.reject.motive', string='Motivo de rechazo')
    price = fields.Float(string='Importe a pagar')
    review = fields.Text(string='Resumen de la evaluación')
    answer_ids = fields.One2many('gradein.answer', 'relacion_id', string='Respuestas')
    question_id = fields.Many2one('gradein.question', string='Pregunta')
    answer_id = fields.Many2one('gradein.answer', string='Respuesta dada')
