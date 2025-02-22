from odoo import fields, models

class BillboardSala(models.Model):
    _name = "billboard.sala"

    nombre = fields.Char(required=True)
    capacidad = fields.Integer(required=True, default=1)
    tipoDeSala = fields.Selection(selection=[
        ('2D', '2D'),
        ('3D', '3D'),
        ('IMAX', 'IMAX'),
        ('VIP', 'VIP'),
    ])
    estado = fields.Selection(selection=[
        ('Disponible', 'Disponible'),
        ('En mantenimiento', 'En mantenimiento'),
        ('Ocupada', 'Ocupada'),
    ], default='Disponible'
    )
     # Relación One2many con el modelo "Funcion"
    funciones_ids = fields.One2many('billboard.funcion', 'sala', string="Funciones")