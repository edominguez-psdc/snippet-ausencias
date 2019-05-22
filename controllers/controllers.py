# -*- coding: utf-8 -*-
from odoo import http

# class Snippet-ausencia(http.Controller):
#     @http.route('/snippet-ausencia/snippet-ausencia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/snippet-ausencia/snippet-ausencia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('snippet-ausencia.listing', {
#             'root': '/snippet-ausencia/snippet-ausencia',
#             'objects': http.request.env['snippet-ausencia.snippet-ausencia'].search([]),
#         })

#     @http.route('/snippet-ausencia/snippet-ausencia/objects/<model("snippet-ausencia.snippet-ausencia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('snippet-ausencia.object', {
#             'object': obj
#         })