{
    'name': "Hospital Management",
    'version': '17.0.1.0.0',
    'summary': 'Hospital Management',
    'description': """Hospital Management system""",

    'author': "Teckzilla",
    'website': "https://www.teckzilla.net/",
    'category': 'Hospital Management system',
    'sequence': -100,
    'depends': ['base','mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
    ],
    'images': ['static/description/icon.png'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,

}
