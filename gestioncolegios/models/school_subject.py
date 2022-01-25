from odoo import models, fields


class subject(models.Model):
    _name = 'school.subject'
    _description = 'Relacion de los cursos del colegio'
    #
    # name = fields.Many2one('school.teacher', string="Nombre del curso", required=True)
    name = fields.Char(string="Nombre del curso", required=True)
    credits = fields.Integer(required=True)
    max_students = fields.Integer(required=True)
    active = fields.Boolean(string="¿Curso activo?", required=True)

    # Claves foraneas
    teacher_id = fields.Many2one('school.teacher', string='Nombre del docente', required=True)
    student_ids = fields.Many2many('school.student', string="Lista de estudiantes")
