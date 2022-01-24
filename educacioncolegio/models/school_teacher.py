from odoo import models, fields

class subject(models.Model):
    _name = 'school.subject'
    _description = 'Relacion de los cursos del colegio'

    # name = fields.Char(string="Nombre del docente", required=True)
    # profile = fields.Text(string='Perfil')
    # subject_ids = fields.One2many('school.subject', 'name', string="Cursos del docente")
    #
