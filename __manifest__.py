{
    'name': 'Import Order Lines',
    'version': 'v16',
    'summary': 'Import Order Line from XLSX File',
    'description': 'Import Sale & Purchase Order Line from XLSX File',
    'license': 'LGPL-3',
    'author': 'Shawon',
    'depends': ['report_xlsx', 'purchase', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/import_pol_wiz_view.xml',
        'wizard/import_sol_wiz_view.xml',
        'views/purchase_view.xml',
        'views/sale_view.xml',
        'report/sample_xlsx.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False
}
