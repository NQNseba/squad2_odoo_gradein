from odoo import models, api

class GradeInOrderReport(models.AbstractModel):
    _name = 'report.gradein_services.gradein_order_report' ##Se deja comentario de que el error se daba porque era necesario conectar el modulo completo, no el modelo de Grade In Order
    _report_name = 'gradein_order_report'
    _description = 'Grade In Order Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        if data and data.get('docs'):
            docids = data.get('docs')
        docs = self.env['gradein.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'gradein.order',
            'docs': docs,
        }