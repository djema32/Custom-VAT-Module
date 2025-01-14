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
    'support': 'Xander.djema@gmail.com',
    'repository': 'https://github.com/djema32/Custom-VAT-Module#18.0',
    'description': '
    # VAT Price Display Module

This module enables the display of both **VAT-exclusive** and **VAT-inclusive** prices for your products on your Odoo eCommerce store. This feature helps customers see the actual price of products without VAT (for wholesale or business purchases) alongside the final price with VAT (for retail customers).

## Features:
- Displays **both VAT-exclusive** and **VAT-inclusive** prices on product pages, so customers can easily compare.
- **Easy to install and configure** in Odoo's eCommerce system.
- **Supports multiple tax rules**, making it flexible for businesses operating under different VAT rates or conditions.
- Customizable display options for both prices, depending on the product or customer.

## Installation Instructions:
1. Download the module and place it in your custom add-ons directory.
2. Go to **Apps**, click **Update Apps List**, and search for "**VAT Price Display**".
3. Click **Install** to add the module to your Odoo system.
4. Configure the display settings for VAT-exclusive and VAT-inclusive prices from the eCommerce settings.

## Support:
For any issues or further customization requests, contact: [Xander.djema@gmail.com](mailto:Xander.djema@gmail.com)

## License:
LGPL-3

## Repository:
You can find the source code and contribute here: [GitHub Repository](https://github.com/djema32/Custom-VAT-Module)

    '
}
