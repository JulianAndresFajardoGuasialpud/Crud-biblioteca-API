# View: Una vista es una función de gestión de peticiones que recibe peticiones HTTP y devuelve respuestas HTTP. Las vistas acceden a los datos que necesitan para satisfacer las peticiones por medio de modelos, y delegan el formateo de la respuesta a las plantillas ("templates").
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Importaciones propias
from .models import Book
from .serializers import BookSerializers

# Create your views here.


@api_view(['GET'])
def getBooks(request):
    book = Book.objects.all()
    serializer = BookSerializers(book, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postBooks(request):
    if request.method == "POST":
     data = request.data
    book = Book.objects.create(
        #Error para guardar el dato el arreglo
        body = data
    )
    serializer = BookSerializers(book, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def putBooks(request, pk):
    data = request.data
    book = Book.objects.get(id=pk)
    serializer = BookSerializers(instance=book, data= data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteBooks(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return Response("Book delete")
