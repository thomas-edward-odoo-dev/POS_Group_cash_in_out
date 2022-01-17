# -*- coding: utf-8 -*-
# from odoo import http


# class AtumPosGroupCashInOut(http.Controller):
#     @http.route('/atum_pos_group_cash_in_out/atum_pos_group_cash_in_out/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/atum_pos_group_cash_in_out/atum_pos_group_cash_in_out/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('atum_pos_group_cash_in_out.listing', {
#             'root': '/atum_pos_group_cash_in_out/atum_pos_group_cash_in_out',
#             'objects': http.request.env['atum_pos_group_cash_in_out.atum_pos_group_cash_in_out'].search([]),
#         })

#     @http.route('/atum_pos_group_cash_in_out/atum_pos_group_cash_in_out/objects/<model("atum_pos_group_cash_in_out.atum_pos_group_cash_in_out"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('atum_pos_group_cash_in_out.object', {
#             'object': obj
#         })
