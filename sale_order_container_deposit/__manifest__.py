{
    'name': 'Sale Order Container Deposit',
    'version': '16.0.1.0.0',
    'summary': 'Show total quantities of regular vs container (deposit) products on sale orders',
    'category': 'Sales',
    'author': 'Local Dev',
    'depends': ['sale', 'product'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}