{
    'name': 'Display Product Price Including & Excluding VAT',
    'version': '1.0',  # Correct version format for Odoo 18
    'summary': 'Show product price excluding VAT alongside the including VAT price.',
    'author': 'Xander Djema',
    'category': 'Website & eCommerce',
    'website': 'http://www.djema.be',
    'depends': ['website_sale'],  # Ensure the dependency is listed
    'data': [
        'views/products_vat_template.xml',  # Templates for product display
        'views/product_vat_template.xml',   # Additional views if needed
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'currency': 'EUR',
    'price': 75.00,  # Add the price of your module
    'support': 'Xander.djema@gmail.com',  # Support email
    'repository': 'https://github.com/djema32/Custom-VAT-Module#18.0',  # Repository URL with the correct branch for Odoo 18.0
    'icon': '/custom_vat_module/static/description/icon.png',  # Path to the module's icon
}
