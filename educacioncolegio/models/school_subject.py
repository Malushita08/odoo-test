from odoo import models, fields


class subject(models.Model):
    _name = 'school.subject'
    _description = 'Relacion de los cursos del colegio'
    #
    # name = fields.Char(string="Nombre del curso", required=True)
    # credits = fields.Integer(required=True)
    # max_students = fields.Integer(required=True)
    # active = fields.Boolean(string="", required=True)
    # student_ids = fields.Many2many('school.student',string="Lista de estudiantes")
    # teacher_id = fields.Many2one('school.teacher', string="Id del docente", required=True)
