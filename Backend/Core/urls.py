# Imports django Users
from django.contrib import admin
from django.urls import path, include

# Imports django REST framework
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework import routers

# Imports of swagger for testing APIs
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Import ModelViews users
from Users import views

# Import biblioteca router
from biblioteca.api.routerBiblioteca import router_biblioteca

# Scheme swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Test APIS",
        default_version='v1',
        description="Test",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# RegisterView Users
router.register(
    r'users',
    views.UserViewSet,
    basename='users'
)

# RegisterView Groups Users
router.register(
    r'groups',
    views.GroupViewSet,
    basename='groups'
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # URLS from swagger
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),

    # URLS routers
    path('', include(router.urls)),

    # Views django users

    # Views biblioteca API
"""     path('api/', include(router_biblioteca)), """
]
