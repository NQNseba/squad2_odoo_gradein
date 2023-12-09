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
    equipment = fields.Many2one('gradein_equipment', string='Equipo')
    imei = fields.Integer(string='IMEI')
    image = fields.Many2many('ir.attachment', string='Imagen')
    partner_id = fields.Many2one('res.partner', string='Cliente')
    ##reject_motive_id = fields.Many2one('gradein.reject.motive', string='Motivo de rechazo')
    price = fields.Float(string='Importe a pagar')
    review = fields.Text(string='Resumen de la evaluación')
    answer_ids = fields.One2many('gradein.answer', string='Respuestas')
    question_id = fields.Many2one('gradein.question', string='Pregunta')
    answer_ids = fields.Many2one('gradein.answer', string='Respuesta dada')
