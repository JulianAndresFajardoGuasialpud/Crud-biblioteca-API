from rest_framework import serializers
from biblioteca.models import Book, Genre, Author, Language, BookInstance

# Books
class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Genre
class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# Author
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# Language
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

# books instance
class BookInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookInstance
        fields = '__all__'