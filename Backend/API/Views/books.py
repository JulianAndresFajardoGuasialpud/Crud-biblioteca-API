# View: Una vista es una función de gestión de peticiones que recibe peticiones HTTP y devuelve respuestas HTTP. Las vistas acceden a los datos que necesitan para satisfacer las peticiones por medio de modelos, y delegan el formateo de la respuesta a las plantillas ("templates").

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Importaciones propias
from ..models import Book
from ..serializers import BookSerializers

# Create your views here.


@api_view(['GET'])
def getBooks(request):
    book = Book.objects.all().order_by('id_book', 'data')
    serializer = BookSerializers(book, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postBooks(request):
    if request.method == "POST":

        data = request.data

        book = Book.objects.create(
            data=data
        )
        serializer = BookSerializers(book, many=False)
        return Response(serializer.data)


@api_view(['PUT'])
def putBooks(request, id_book):
    data = request.data
    book = Book.objects.get(
        id_book=id_book
    )
    serializer = BookSerializers(instance=book, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteBooks(request, id_book):
    book = Book.objects.get(
        id_book=id_book
    )
    book.delete()
    return Response("Book delete")
