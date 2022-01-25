# -*- coding: utf-8 -*-
# from odoo import http


# class Gestioncolegios(http.Controller):
#     @http.route('/gestioncolegios/gestioncolegios', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestioncolegios/gestioncolegios/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestioncolegios.listing', {
#             'root': '/gestioncolegios/gestioncolegios',
#             'objects': http.request.env['gestioncolegios.gestioncolegios'].search([]),
#         })

#     @http.route('/gestioncolegios/gestioncolegios/objects/<model("gestioncolegios.gestioncolegios"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestioncolegios.object', {
#             'object': obj
#         })
