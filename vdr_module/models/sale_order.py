# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def write(self, values):
        raise UserError(_("EGO warning."))
        res = super(SaleOrderLine, self).write(values)
        return res