# Models: Los Modelos son objetos de Python que definen la estructura de los datos de una aplicación y proporcionan mecanismos para gestionar (añadir, modificar y borrar) y consultar registros en la base de datos.

from django.db import models

# Create your models here.
# aqui se crea los modelos de la base de datos relacionales


class Book(models.Model):
    body = models.CharField(
        max_length=50
    )

    class Meta:
        ordering = ['id', 'body']

    def __str__(self):
        return self.body
