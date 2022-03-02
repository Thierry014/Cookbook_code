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
        'views/library_book_rent.xml',
        # 'data/data.xml'
        'wizard/rent_book_wiz.xml',
        'wizard/return_book_wiz.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],

    # auto_install
}