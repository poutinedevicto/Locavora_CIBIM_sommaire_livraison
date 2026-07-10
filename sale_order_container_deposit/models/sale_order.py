from odoo import models, fields, api

# Category name used to identify container/deposit products (provided by user)
CONTAINER_CATEGORY_NAME = 'contenant_consigne'


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Expose customer tags (partner categories) directly on the sale.order
    partner_tag_ids = fields.Many2many('res.partner.category', related='partner_id.category_id', string='Customer Tags', store=True)

    total_qty_regular = fields.Float(string='Total Qty (regular)', compute='_compute_total_qtys', store=True)
    total_qty_container_deposit = fields.Float(string='Total Qty (container/deposit)', compute='_compute_total_qtys', store=True)

    @api.depends('order_line.product_uom_qty', 'order_line.product_id', 'order_line.product_id.categ_id')
    def _compute_total_qtys(self):
        for order in self:
            total_regular = 0.0
            total_container = 0.0
            for line in order.order_line:
                qty = line.product_uom_qty or 0.0
                prod = line.product_id
                is_container = False
                if prod and prod.categ_id:
                    categ = prod.categ_id
                    # walk up parent categories to allow nested category match
                    while categ:
                        if categ.name == CONTAINER_CATEGORY_NAME:
                            is_container = True
                            break
                        categ = categ.parent_id
                if is_container:
                    total_container += qty
                else:
                    total_regular += qty
            order.total_qty_regular = total_regular
            order.total_qty_container_deposit = total_container
