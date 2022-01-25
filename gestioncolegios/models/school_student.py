from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


class student(models.Model):
    _name = 'school.student'
    _description = 'Relacion de los estudiantes del colegio'

    name = fields.Char(string="Nombre del estudiante", required=True)
    birth_date = fields.Date(string="Fecha de nacimiento", required=True)
    age = fields.Integer(compute="_calculate_age", store=True)
    final_exam_grade = fields.Float(required=True)

    # Claves foraneas
    subject_ids = fields.Many2many('school.subject', string="Lista de cursos")

    # Campos extra
    approved = fields.Boolean(compute="_is_approved", store=False)
    # nro_cursos = fields.Boolean(compute="_calculate_age", store=False, string="Aprobado")

    # Calcular la edad
    @api.depends('birth_date')
    def _calculate_age(self):
        for record in self:
            edad = relativedelta(datetime.now(), record.birth_date)
            record.age = int(edad.years)

    # Calcular si el alumno está aprobado
    @api.depends('final_exam_grade')
    def _is_approved(self):
        for record in self:
            if (record.final_exam_grade >= 14):
                record.approved = True
            else:
                record.approved = False
