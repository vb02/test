import uuid

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PosAdvertisment(models.Model):
    _name = 'pos.advertisment.line'


    pos_advertisment_id = fields.Many2one('pos.config',string="Not neccesary")
    image = fields.Binary(string="Image")
    name = fields.Char(string="Name")
    sequence = fields.Integer(string='Sequence')
    duration = fields.Char(string="Duration")
    description = fields.Text(string="Description")