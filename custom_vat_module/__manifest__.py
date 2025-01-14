{
    'name': 'Custom VAT Module',
    'version': '1.0.0.1',
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
    'support': 'Xander.djema@gmail.com',
    'repository': 'https://github.com/djema32/Custom-VAT-Module#18.0',
    'description': ' 
# VAT Price Display Module

This module allows you to display both VAT-exclusive and VAT-inclusive prices for your products.

## Features:
- Show both VAT-exclusive and VAT-inclusive prices on product pages.
- Easy to install and configure in Odoo eCommerce.
- Supports multiple tax rules.

## Installation Instructions:
1. Download the module and place it in the custom add-ons directory.
2. Go to Apps, click Update Apps List, and search for "VAT Price Display".
3. Click Install to add the module to your Odoo system.

## Support:
For support, contact: [Xander.djema@gmail.com](mailto:Xander.djema@gmail.com)
' 

}
