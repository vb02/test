import uuid

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PosConfig(models.Model):
    _inherit = 'pos.config'

    advertisment_line = fields.One2many('pos.advertisment.line','pos_advertisment_id',string="Advertisment")

