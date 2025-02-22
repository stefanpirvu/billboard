{
    'name': 'billboard',
    'application': True,
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/billboard_pelicula_views.xml',
        'views/billboard_sala_views.xml',
        'views/billboard_funcion_views.xml',
        'views/billboard_menus.xml',
    ],
}
