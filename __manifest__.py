{
    'name' : 'Bista Test Addon',
    'version' : '1.1',
    'summary': 'Bista Test Addon',
    'sequence': 2,
    'description': """Bista Addons""",
    'depends' : ['base','sale','contacts'],
    'data': [
        'views/test_views.xml',
        'views/test1_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
