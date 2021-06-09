{
    "name":"openacademy",
    "summary": """Manage trainings""",

    'descripcion':"""
        Open Academy module for managin trainins:
            - training courses
            - training sessions
            - attendees registration
    """,
    'author': "My Company",
    'website': "http:/www.yourcompany.com",

    'category': 'test',
    'version': '0.1',

    'depends': ['base'],

    'data':[
        'security/ir.model.access.csv',
        'views/openacademy.xml'
    ],
    
    'demo':[
        'demo/demo.xml',
        ],
}