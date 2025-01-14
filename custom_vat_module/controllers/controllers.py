# -*- coding: utf-8 -*-
# from odoo import http


# class CustomVatModule(http.Controller):
#     @http.route('/custom_vat_module/custom_vat_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_vat_module/custom_vat_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_vat_module.listing', {
#             'root': '/custom_vat_module/custom_vat_module',
#             'objects': http.request.env['custom_vat_module.custom_vat_module'].search([]),
#         })

#     @http.route('/custom_vat_module/custom_vat_module/objects/<model("custom_vat_module.custom_vat_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_vat_module.object', {
#             'object': obj
#         })

