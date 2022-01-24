# -*- coding: utf-8 -*-
from odoo import http

# class Educacioncolegio(http.Controller):
#     @http.route('/educacioncolegio/educacioncolegio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/educacioncolegio/educacioncolegio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('educacioncolegio.listing', {
#             'root': '/educacioncolegio/educacioncolegio',
#             'objects': http.request.env['educacioncolegio.educacioncolegio'].search([]),
#         })

#     @http.route('/educacioncolegio/educacioncolegio/objects/<model("educacioncolegio.educacioncolegio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('educacioncolegio.object', {
#             'object': obj
#         })