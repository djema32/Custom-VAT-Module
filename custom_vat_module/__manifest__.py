{
    'name': 'Display Product Price Including & Excluding VAT',
    'version': '1.0',
    'summary': 'Show product price excluding VAT alongside the including VAT price.',
    'author': 'Xander Djema',
    'category': 'Website & eCommerce',
    'website': 'http://www.djema.be',
    'depends': ['website_sale'],
    'data': [
        'views/products_vat_template.xml',
        'views/product_vat_template.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'currency': 'EUR',
    'price': 75.00,
    'images': {
        'thumbnail': 'static/description/cover.png',
        # You can add more images if needed
        'icon': 'static/description/cover.jpg',
    },
    'support': 'Xander.djema@gmail.com',
    'repository': 'https://github.com/djema32/Custom-VAT-Module#18.0',
    'description': 'This module enables the display of both VAT-exclusive and VAT-inclusive prices for products on your Odoo eCommerce store, making it easier for customers to see both price options. For the full documentation, go to this webpage: [Djema.be](http://www.djema.be).',
}
