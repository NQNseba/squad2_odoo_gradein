# gradein_equipment_type_search_view.py
from odoo import api, fields, models

class GradeInEquipmentType(models.Model):
    _inherit = 'gradein.equipment.type'

    # Agregar vista de búsqueda
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        result = super(GradeInEquipmentType, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if view_type == 'search':
            # Personalizar la vista de búsqueda según tus necesidades
            search_view = """
                <search string="Buscar Tipos de Equipos">
                    <field name="name" string="Nombre" filter_domain="[['name', 'ilike', self]]"/>
                    <field name="active" string="Activo" filter_domain="[['active', '=', self]]"/>
                </search>
            """
            result['arch'] = search_view
        return result
