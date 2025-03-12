{
    'name': "DiazRomeroSantiago",
    'summary': "Módulo personalizado para gestionar información zodiacal y redes sociales de contactos.",
    'description': """
        Este módulo extiende el modelo res_partner para añadir campos como:
        - Fecha de nacimiento.
        - Edad (calculada automáticamente).
        - Signo zodiacal (calculado automáticamente).
        - Perfil de LinkedIn.
        - Estado de actividad en redes sociales (calculado automáticamente).
    """,
    'author': "Santiago Diaz Romero",
    'website': "https://github.com/sromerodiaz-dc",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'contacts'],
    'data': [
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}