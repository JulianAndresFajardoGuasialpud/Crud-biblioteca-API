from django.db import models
from django.urls import reverse
import uuid  # Requerida para las instancias de libros únicos


# Model for genre books


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
    )

    def __str__(self) -> str:
        return self.name

# Model for Book (table master)


class Book(models.Model):
    """
    Modelo que representa un libro (pero no un Ejemplar específico).
    """
    title = models.CharField(
        max_length=100,
    )
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL, null=True
    )
    summary = models.TextField(
        max_length=1000,
        help_text='Ingrese una breve descripción del libro'
    )
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
    )
    # ManyToManyField, porque un género puede contener muchos libros y un libro puede cubrir varios géneros.
    # La clase Genre ya ha sido definida, entonces podemos especificar el objeto arriba.
    genre = models.ManyToManyField(
        Genre,
        help_text='Seleccione un genero para este libro'
    )
    """
    String que representa al objeto Book
    """
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('book-detail', args=[str(self.id)]) # type: ignore

# Model for BookInstance


class BookInstance(models.Model):
    """
    Modelo que representa una copia específica de un libro (i.e. que puede ser prestado por la biblioteca).
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID único para este libro particular en toda la biblioteca"
    )
    book = models.ForeignKey(
        'Book',
        on_delete=models.SET_NULL, null=True
    )
    imprint = models.CharField(
        max_length=200,
    )
    due_back = models.DateField(
        null=True,
        blank=True,
    )
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Disponibilidad del libro',
    )
    class Meta:
        ordering = ["due_back"]
    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id, self.book.title) # type: ignore
