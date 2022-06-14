# -*- coding: utf-8 -*-
# from odoo import http


# class First-test-module(http.Controller):
#     @http.route('/first-test-module/first-test-module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/first-test-module/first-test-module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('first-test-module.listing', {
#             'root': '/first-test-module/first-test-module',
#             'objects': http.request.env['first-test-module.first-test-module'].search([]),
#         })

#     @http.route('/first-test-module/first-test-module/objects/<model("first-test-module.first-test-module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('first-test-module.object', {
#             'object': obj
#         })
