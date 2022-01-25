# -*- coding: utf-8 -*-
{
    'name': "gestioncolegios",

    'summary': """
        Modulo de prueba para la gestion de alumnos, cursos y docentes""",

    'description': """
        Modulo de prueba para la gestion de alumnos, cursos y docentes
    """,

    'author': "Maria Luisa Cáceres Loayza",
    'website': "http://www.malus.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menusyacciones.xml',
        'views/school_teacher.xml',
        'views/school_subject.xml',
        'views/school_student.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
