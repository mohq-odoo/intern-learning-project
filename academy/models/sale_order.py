# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):

    _inherit = "sale.order"

    session_id = fields.Many2many(comodel_name="academy.session",
            string="Related Session",
            ondelete='cascade')
        
    instructor_id = fields.Many2one(string="Session Instructor",
            related='session_id.instructor_id')

    student_ids = fields.Many2many(string="Students",
            related='session_id.student_ids')

    