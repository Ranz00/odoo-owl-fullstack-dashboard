from odoo import http
from odoo.http import request

class DashboardApiController(http.Controller):
    @http.route('/api/v1/dashboard/stats', type='json', auth='user', methods=['POST'])
    def get_external_stats(self):
        # Exposes the dashboard data via a JSON-RPC / REST endpoint
        return request.env['sales.dashboard'].get_stats()
