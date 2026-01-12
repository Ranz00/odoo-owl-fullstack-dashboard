{
    'name': 'Odoo OWL Fullstack Dashboard',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Fullstack Dashboard: OWL, Python, and REST API Integration',
    'depends': ['sale', 'web'],
    'data': [
        'views/dashboard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo-owl-fullstack-dashboard/static/src/js/dashboard.js',
            'odoo-owl-fullstack-dashboard/static/src/xml/dashboard.xml',
        ],
    },
    'installable': True,
    'application': True,
}
