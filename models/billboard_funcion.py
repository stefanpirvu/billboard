from odoo import fields, models, api
from datetime import timedelta 

class BillboardFuncion(models.Model):
    _name = "billboard.funcion"

    # comprobar si está bien así esta relación
    pelicula = fields.Many2one('billboard.pelicula', required=True)
    # comprobar si está bien así esta relación
    sala = fields.Many2one('billboard.sala', required=True)
    fecha_y_hora_inicio = fields.Datetime(required=True)
    fecha_y_hora_fin = fields.Datetime(compute="_calcular_fecha_y_hora_fin_pelicula")
    precio_entrada = fields.Float(required=True )
    estado = fields.Selection(selection=[
        ('Programada', 'Programada'),
        ('En curso', 'En curso'),
        ('Finalizada', 'Finalizada'),
    ],default='Programada')

    @api.depends('fecha_y_hora_inicio')
    def _calcular_fecha_y_hora_fin_pelicula(self):
        for record in self:
            if record.fecha_y_hora_inicio and record.pelicula.duracion:
                # Obtener la duración de la película en minutos
                duracion_minutos = record.pelicula.duracion
                # Calcular la fecha y hora de fin sumando los minutos a la hora de inicio
                record.fecha_y_hora_fin = record.fecha_y_hora_inicio + timedelta(minutes=duracion_minutos)