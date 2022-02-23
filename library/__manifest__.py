{
    'name': "Library",
    'version': '14.0.0.0',
    'author': "HJ",
    'category': 'Category',
    'description': """
    """,
    'depends': ['base'],

    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo_data.xml',
    ],

    # auto_install
}