# -*- coding: utf-8 -*-
# Part of odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleOrder(models.Model):
    """Enable all models to be available for API request."""

    _inherit = "sale.order"

    def _get_update_prices_lines(self):
        """ Hook to exclude specific lines which should not be updated based on price list recomputation """
        return self.order_line.filtered(lambda line: not line.display_type and line.product_id.name!='Down payment')

