# -*- coding: utf-8 -*-
# from odoo import http


# class Tarea15(http.Controller):
#     @http.route('/tarea15/tarea15', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tarea15/tarea15/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tarea15.listing', {
#             'root': '/tarea15/tarea15',
#             'objects': http.request.env['tarea15.tarea15'].search([]),
#         })

#     @http.route('/tarea15/tarea15/objects/<model("tarea15.tarea15"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tarea15.object', {
#             'object': obj
#         })

