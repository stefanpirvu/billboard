from odoo import fields, models

class BillboardPelicula(models.Model):
    _name = "billboard.pelicula"

    titulo = fields.Char(required=True)
    # Recomendación, usar los "tags"
    genero = fields.Selection(selection=[
        ('Acción', 'Acción'),
        ('Drama', 'Drama'),
        ('Comedia', 'Comedia'),
        ('Ciencia Ficción', 'Ciencia Ficción'),
        ('Terror', 'Terror'),
        ('Animación', 'Animación'),
    ])
    duracion = fields.Integer(required=True)
    clasificacion = fields.Selection(selection=[
        ('0', 'Apta para todo los públicos'),
        ('7', 'No recomendada para menores de 7 años'),
        ('12', 'No recomendada para menores de 12 años'),
        ('16', 'No recomendada para menores de 16 años'),
    ])
    fecha_estreno = fields.Date(required=True)
    descripcion = fields.Text()
    imagen_portada = fields.Binary("Portada", attachment=True, required=False)