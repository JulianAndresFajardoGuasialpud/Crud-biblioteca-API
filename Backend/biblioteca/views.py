from django.shortcuts import render

# Create your views here.
@api_view(['GET'])
def getBooks(request):
    book = Book.objects.all()
    serializer = BookSerializers(book, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postBooks(request):
    if request.method == "POST":
        book = Book.objects.create(
        )
        serializer = BookSerializers(book)
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