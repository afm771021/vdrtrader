# -*- coding: utf-8 -*-
# from odoo import http


# class VdrModule(http.Controller):
#     @http.route('/vdr_module/vdr_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vdr_module/vdr_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vdr_module.listing', {
#             'root': '/vdr_module/vdr_module',
#             'objects': http.request.env['vdr_module.vdr_module'].search([]),
#         })

#     @http.route('/vdr_module/vdr_module/objects/<model("vdr_module.vdr_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vdr_module.object', {
#             'object': obj
#         })
