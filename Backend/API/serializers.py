from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Book, Author, Genre, lenguage

# Serializer for methods book view
# Serializers define the API representation.


class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id_book",
            "title_book",
            "description",
            "isbn_book"
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'is_staff',
            'groups'
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url',
            'name'
        ]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id_author',
            'name_author',
            'date_of_birth',
            'date_of_death'
        ]


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = [
            'id_genre',
            'nombre_Genre'
        ]


class LenguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = lenguage
        fields = [
            'id_lenguage ',
            'name_lenguage'
        ]
