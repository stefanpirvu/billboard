from odoo import fields, models, api

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
        # necesito acceder a la duración de la película


• Película (Many2one con cine.pelicula, obligatorio)
• Sala (Many2one con cine.sala, obligatorio)
• Fecha y hora de fin (Datetime, calculado)