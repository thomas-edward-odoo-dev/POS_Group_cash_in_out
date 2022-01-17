# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class atum_pos_group_cash_in_out(models.Model):
#     _name = 'atum_pos_group_cash_in_out.atum_pos_group_cash_in_out'
#     _description = 'atum_pos_group_cash_in_out.atum_pos_group_cash_in_out'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
