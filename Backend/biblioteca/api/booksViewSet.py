from rest_framework import viewsets
from rest_framework import permissions
from biblioteca.models import Book, Author, Genre, Language, BookInstance

# Serializers
from biblioteca.api.booksSerializers import BooksSerializer, GenreSerializer, AuthorSerializer, LanguageSerializer, BookInstanceSerializer

# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.AllowAny]
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.AllowAny]

class ViewSet(viewsets.ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
    permission_classes = [permissions.AllowAny]