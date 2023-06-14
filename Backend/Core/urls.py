"""Core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Imports django Users
from django import views
from django.contrib import admin
from django.urls import path, include

# Imports django REST framework
from rest_framework import permissions

# Imports of swagger for testing API
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Imports django REST framework
from rest_framework import routers

from ..StoneTec.views import UserViewSet, GroupViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="StoneTec",
        default_version='v1',
        description="Test",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # Django users
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # URLS from swagger
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    
    # URLS router
    path('', include(router.urls))
]
