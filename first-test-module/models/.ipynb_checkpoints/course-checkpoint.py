# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'academy.course'
    _description = 'Academy Course Info'

    name = fields.Char(string='Title', required=True)
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(string='Description')
    
    levels = fields.Selection(string='Level',
                             selection=[('beginner', 'Beginner'),
                                       ('medium', 'Medium'),
                                       ('advanced', 'Advanced')],
                             copy=False)
    active = fields.Boolean(string='Active', default=True)
    
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
