from odoo import fields, models

class BillboardSala(models.Model):
    _name = "billboard.sala"
    _rec_name = "nombre"

    nombre = fields.Char(required=True)
    capacidad = fields.Integer(required=True)
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
    funciones_ids = fields.One2many('billboard.funcion', 'sala', string="Funciones")

    _sql_constraints = [
        ('cantidad_min', 'CHECK(cantidad >= 1)', 'La cantidad debe ser mayor o igual a 1.')
    ]