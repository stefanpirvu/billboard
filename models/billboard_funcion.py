from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError

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

    @api.onchange('pelicula')
    def _onchange_pelicula(self):
        if self.pelicula and self.fecha_y_hora_inicio and self.pelicula.duracion:
            self.fecha_y_hora_fin = self.fecha_y_hora_inicio + timedelta(minutes=self.pelicula.duracion)
        else:
            self.fecha_y_hora_fin = False

    def action_iniciar_funcion(self):
        """Método para iniciar la función cambiando el estado a 'En curso'."""
        for record in self:
            record.estado = 'En curso'

    @api.constrains('sala')
    def _check_sala_not_in_maintenance(self):
        for record in self:
            if record.sala and record.sala.estado == 'En mantenimiento':
                raise ValidationError("No se pueden asignar funciones a salas en mantenimiento.")
            
    _sql_constraints = [
        ('fecha_inicio_menor_fin', 
         'CHECK(fecha_y_hora_inicio <= fecha_y_hora_fin)', 
         'La fecha de inicio debe ser menor o igual que la fecha de fin.')
    ]
