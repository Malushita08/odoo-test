from odoo import models, fields


class teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Relacion de docentes del colegio'

    name = fields.Char(string='Nombre del docente', required=True)
    profile = fields.Text(string='Perfil')

    # Claves foraneas
    subject_ids = fields.One2many('school.subject', 'teacher_id', string="Cursos del docente")
