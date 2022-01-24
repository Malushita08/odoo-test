from odoo import models, fields

class subject(models.Model):
    _name = 'school.subject'
    _description = 'Relacion de los cursos del colegio'

    # name = fields.Char(string="Nombre del estudiante", required=True)
    # birth_date = fields.Date(string="Fecha de nacimiento", required=True)
    # age = fields.Integer(required=True)
    # final_exam_grade = fields.Float(required=True)
    # subject_ids = fields.Many2many('school.subject', string="Lista de cursos")
