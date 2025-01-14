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
    'description': """
        <h2>Display Product Price Including & Excluding VAT</h2>
        <p>This module allows you to show both the product price including VAT and excluding VAT on the product page.</p>

        <h3>Features:</h3>
        <ul>
            <li>Display prices with VAT included and excluded</li>
            <li>Simple and easy to install</li>
            <li>Compatible with Odoo's <strong>Website & eCommerce</strong> module</li>
            <li>Shows VAT-exclusive and VAT-inclusive prices on product pages</li>
        </ul>

        <h3>Usage:</h3>
        <p>Once installed, the module automatically updates the product display to show both price options.</p>

        <h3>Requirements:</h3>
        <ul>
            <li>Odoo version 18.0 or higher</li>
            <li>Website Sale module</li>
        </ul>

        <h3>Support:</h3>
        <p>If you encounter any issues, feel free to contact us at <a href="mailto:Xander.djema@gmail.com">Xander.djema@gmail.com</a>.</p>
    """,
}
