from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from authentication.views import Signup, CompleteProfileSerializerView
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('authentication.urls')),
    path('', include('Profile.urls')),
    path('admin/', admin.site.urls)
]


 # urlpatterns = format_suffix_patterns(urlpatterns)
