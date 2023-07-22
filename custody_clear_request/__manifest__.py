{
    'name': 'Custody Clear Request',
    'version': '1.0',
    'category': 'Accounting',
    'author': 'SGT',
    'support': 'info@softguidetech.com',
    'website': 'https://softguidetech.com',
    'license': 'OPL-1',
    'price': '18',
    'currency': 'EUR',
    'data': [

        'security/security_view.xml',
        'security/ir.model.access.csv',
        'views/custody_clear_request_view.xml',
        'views/custody_approval_route.xml',
        'views/res_config_settings_views.xml',
        'data/custody_approval_route.xml',
        'reports/custody_report.xml',
    ],
    'images': [
        'static/description/logo.png',
    ],
    'depends': ['base','account','analytic','custody_request'],




    'installable': True,
    'application': True,






}
