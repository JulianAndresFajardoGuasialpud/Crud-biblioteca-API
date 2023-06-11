# Models: Los Modelos son objetos de Python que definen la estructura de los datos de una aplicación y proporcionan mecanismos para gestionar (añadir, modificar y borrar) y consultar registros en la base de datos.

from django.db import models

# Create your models here.
# aqui se crea los modelos de la base de datos relacionales


class Book(models.Model):
    id_book = models.AutoField(
        primary_key=True,
    )
    title_book = models.CharField(
        editable=True,
        max_length=100
    )
    description = models.TextField(
        editable=True,
        max_length=200
    )
    isbn_book = models.TextField(
        editable=True,
        max_length=100
    )
    class Meta:
        ordering = ['id_book', 'title_book', 'description', 'isbn_book']

    def __str__(self):
        return self.description


# Author
class Author(models.Model):
    id_author = models.AutoField(
        primary_key=True
    )
    name_author = models.TextField(
        max_length=50
    )
    date_of_birth = models.DateField(
        editable=True
    )
    date_of_death = models.DateField(
        editable=True
    )
    id_book = models.ForeignKey(
        Book,
        default=True,
        on_delete=models.CASCADE,
        related_name='id_book_author'
    )
    class Meta:
         ordering = ['name_author', 'date_of_birth', 'date_of_death', 'id_book']
        
    def __str__(self):
        return self.name_author

# Genre


class Genre(models.Model):
    id_genre = models.AutoField(
        primary_key=True
    )
    nombre_Genre = models.TextField(
        max_length=100
    )

    def __str__(self):
        return self.nombre_Genre

# Lenguage


class lenguage(models.Model):
    id_lenguage = models.AutoField(
        primary_key=True
    )
    name_lenguage = models.TextField(
        max_length=100
    )

    def __str__(self):
        return self.name_lenguage
