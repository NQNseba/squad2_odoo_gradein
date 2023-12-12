{
    "name": "Servicios",
    "version": "1.0",
    "author": "Alkemy_Squad2",
    "depends": ["base"],
    "installable": True,
    "application": True,
    "data": [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/gradein_equipment_views.xml',
        'views/gradein_equipment_type_views.xml',
        'views/gradein_question_views.xml',
        'views/gradein_answer_views.xml',
        'views/gradein_reject_motive_views.xml',
        'views/gradein_image_views.xml',
        'views/gradein_order_views.xml',
        'views/menu_gradein.xml',
        'reports/gradein_order_report_views.xml',
    ],
    'images': [
        'static/description/icon.png',
    ],
}