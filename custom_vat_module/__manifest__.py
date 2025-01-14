{
    'name': 'Custom VAT Module',
    'version': '1.0',
    'summary': 'Show product price excluding VAT alongside the including VAT price.',
    'author': 'Xander Djema',
    'category': 'Website & eCommerce',
    'website': 'http://www.djema.be',
    'depends': ['website_sale'],  # Ensure the dependency is listed
    'data': [
        'views/products_vat_template.xml',    # Templates for product display
        'views/product_vat_template.xml',     # Additional views if needed
    ],
    'installable': True,
    'application': False,
}
