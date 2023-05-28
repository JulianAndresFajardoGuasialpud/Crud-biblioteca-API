#URLs: Aunque es posible procesar peticiones de cada URL individual vía una función individual, es mucho más sostenible escribir una función de visualización separada para cada recurso. Se usa un mapeador URL para redirigir las peticiones HTTP a la vista apropiada basándose en la URL de la petición. El mapeador URL se usa para redirigir las peticiones HTTP a la vista apropiada basándose en la URL de la petición. El mapeador URL puede también emparejar patrones de cadenas o dígitos específicos que aparecen en una URL y los pasan a la función de visualización como datos.

from django.urls import path
from API.Views import books


urlpatterns = [
    path('get/', books.getBooks),
    path('post/', books.postBooks),
    path('put/<int:pk>/', books.putBooks),
    path('delete/<int:pk>/', books.deleteBooks),
]
