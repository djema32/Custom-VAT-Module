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
    <h1>VAT Price Display Module</h1>
    <p>This module allows you to display both VAT-exclusive and VAT-inclusive prices for your products.</p>
    
    <h2>Features:</h2>
    <ul>
        <li>Show both VAT-exclusive and VAT-inclusive prices on product pages.</li>
        <li>Easy to install and configure in Odoo eCommerce.</li>
        <li>Supports multiple tax rules.</li>
    </ul>

    <h2>Installation Instructions:</h2>
    <ol>
        <li>Download the module and place it in the custom add-ons directory.</li>
        <li>Go to Apps, click Update Apps List, and search for "VAT Price Display".</li>
        <li>Click Install to add the module to your Odoo system.</li>
    </ol>

    <h2>Usage:</h2>
    <p>After installation, the module will automatically display both VAT-exclusive and VAT-inclusive prices on your product pages in the website's product listings and detailed views.</p>

    <h2>Support:</h2>
    <p>If you encounter any issues or need help, please reach out to <a href="mailto:Xander.djema@gmail.com">Xander.djema@gmail.com</a></p>
"""
}
