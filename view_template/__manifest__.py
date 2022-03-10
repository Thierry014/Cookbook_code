{
    'name': "Hj14 View Module",
    'version': '14.0.0.0',
    'depends': ['base'],
    'author': "HJ",
    'category': 'Category',
    'description': """
    All view practice
    """,
    'depends': ['base','mail'],

    'data': [
        'views/henry_view.xml',
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],

    # auto_install
}