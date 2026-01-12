/** @odoo-module **/
import { registry } from "@web/core/registry";
const { Component, onWillStart, useState } = owl;
import { useService } from "@web/core/utils/hooks";

class SalesDashboard extends Component {
    setup() {
        this.rpc = useService("rpc");
        this.state = useState({ stats: { count: 0, total_amount: 0, currency: '$' } });

        onWillStart(async () => {
            await this.loadData();
        });
    }

    async loadData() {
        const data = await this.rpc("/web/dataset/call_kw/sales.dashboard/get_stats", {
            model: 'sales.dashboard',
            method: 'get_stats',
            args: [],
            kwargs: {},
        });
        this.state.stats = data;
    }
}

SalesDashboard.template = "odoo_owl_dashboard.DashboardMain";
registry.category("actions").add("sales_dashboard_action", SalesDashboard);
