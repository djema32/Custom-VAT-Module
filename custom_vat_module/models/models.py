# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custom_vat_module(models.Model):
#     _name = 'custom_vat_module.custom_vat_module'
#     _description = 'custom_vat_module.custom_vat_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

