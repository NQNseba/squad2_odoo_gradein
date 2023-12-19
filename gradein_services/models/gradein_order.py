from odoo import models, fields, api

class GradeInOrder(models.Model):
    _name = "gradein.order"
    _description = "Grade in Order"

    name = fields.Char(string="Name")
    date = fields.Date(string="Date")
    state = fields.Selection([
        ('draft','Draft'),
        ('confirmed','Confirmed'),
        ('rejected','Rejected'),], string='State', default='draft')
    equipment_id = fields.Many2one('gradein.equipment', string='Equipment')
    imei = fields.Char(string='IMEI')
    image_ids = fields.One2many('gradein.order.image', 'grade_order_id', string='Images')
    partner_id = fields.Many2one('res.partner', string='Client')
    reject_motive_id = fields.Many2one('gradein.reject.motive', string='Reject Motive')
    price = fields.Float(string='Amount to pay')
    review = fields.Text(string='Evaluation Summary')
    question_id = fields.Many2one('gradein.question', string='Question')
    answer_ids = fields.Many2one('gradein.answer', string='Answers')

    @api.onchange('answer_ids')
    def _onchange_answer_ids(self):
        for order in self:
            total_price_reduction = sum(answer.price_reduction for answer in order.answer_ids if answer.active)
            # Asegúrate de no descontar si la cantidad de pago es 0
            order.price = max(0, order.price - total_price_reduction)

