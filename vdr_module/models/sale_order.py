# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_quotation_send(self):
        ''' Opens a wizard to compose an email, with relevant mail template loaded by default '''
        self.ensure_one()

        for order in self:
            _logger.info("ego order: %s", order)
            qty = 0.0
            cont = 0
            for line in order.order_line:
                cont += 1
                _logger.info("ego cont: %d, %f", cont, qty)
                qty += line.product_uom_qty
            _logger.info("ego qty: %f", qty)
            if qty > 10:
                raise UserError(_("EGO warning."))

        response = super(SaleOrder, self).action_quotation_send()

        return response
