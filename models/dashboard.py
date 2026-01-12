from odoo import models, api

class SalesDashboard(models.Model):
    _name = 'sales.dashboard'
    _description = 'Sales Dashboard Logic'

    @api.model
    def get_stats(self):
        # Optimized ORM call that translates to SQL: 
        # SELECT sum(amount_total), count(id) FROM sale_order WHERE state = 'sale'
        orders = self.env['sale.order'].search([('state', '=', 'sale')])
        return {
            'count': len(orders),
            'total_amount': sum(orders.mapped('amount_total')),
            'currency': self.env.company.currency_id.symbol
        }
