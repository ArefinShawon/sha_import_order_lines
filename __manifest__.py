{
    'name': 'Import Order Lines',
    'version': 'v1',
    'summary': 'Import Order Line from XLSX File',
    'description': 'Import Sale & Purchase Order Line from XLSX File',
    'license': 'LGPL-3',
    'sequence': 1,
    'author': 'Hasinur Arefin Shawon',
    'depends': ['report_xlsx', 'purchase'],
    'data': [
        'views/purchase_view.xml',
    ],
    'installable': True,
    'auto_install': False
}
