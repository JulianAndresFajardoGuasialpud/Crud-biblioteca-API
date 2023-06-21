from rest_framework import routers

from biblioteca.api.booksViewSet import BooksViewSet


# Routers provide an easy way of automatically determining the URL conf.
router_biblioteca = routers.DefaultRouter()

# RegisterView biblioteca
router_biblioteca.register(
    prefix='biblioteca',
    basename='biblioteca',
    viewset=BooksViewSet
)