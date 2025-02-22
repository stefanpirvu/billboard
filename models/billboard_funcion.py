from odoo import fields, models, api
from datetime import timedelta

class BillboardFuncion(models.Model):
    _name = "billboard.funcion"

    pelicula = fields.Many2one('billboard.pelicula', required=True)
    sala = fields.Many2one('billboard.sala', required=True)
    fecha_y_hora_inicio = fields.Datetime(required=True)
    fecha_y_hora_fin = fields.Datetime(string="Fecha y Hora de Fin", compute='_compute_fecha_y_hora_fin', store=True)
    precio_entrada = fields.Float(required=True)
    estado = fields.Selection(selection=[
        ('Programada', 'Programada'),
        ('En curso', 'En curso'),
        ('Finalizada', 'Finalizada'),
    ], default='Programada')

    @api.depends('fecha_y_hora_inicio', 'pelicula.duracion')
    def _compute_fecha_y_hora_fin(self):
        for record in self:
            if record.fecha_y_hora_inicio and record.pelicula.duracion:
                record.fecha_y_hora_fin = record.fecha_y_hora_inicio + timedelta(minutes=record.pelicula.duracion)
            else:
                record.fecha_y_hora_fin = False
