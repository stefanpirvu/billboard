from odoo import fields, models

class BillboardProperty(models.Model):
    _name = "billboard.property"

    titulo = fields.Char(required=True)
    anio_lanzamiento = fields.Integer()
    edad_minima = fields.Selection(selection=[
        ('0', 'Apta para todo los públicos'),
        ('7', 'No recomendada para menores de 7 años'),
        ('12', 'No recomendada para menores de 12 años'),
        ('16', 'No recomendada para menores de 16 años'),
    ])
    duracion = fields.Float(string='Duración (horas)', help="Duración en horas y minutos")
    imagen_portada = fields.Binary("Portada", attachment=True, required=False)
    # generos
    # descripcion = fields.Text()
    # valoracion
    # popularidad
    # direccion
    # guion
    # reparto_principal
    # reseñas