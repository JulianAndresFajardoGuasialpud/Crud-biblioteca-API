from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Book

# Serializer for methods book view
# Serializers define the API representation.


class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id_book",
            "title_book",
            "title_book",
            "description",
            "isbn_book"
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
