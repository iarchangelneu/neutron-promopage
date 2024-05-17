from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from neutron.settings import MEDIA_URL, MEDIA_ROOT, DEBUG, STATIC_URL, STATIC_ROOT


schema_view = get_schema_view(
    openapi.Info(
        title="Neutron",
        default_version='v1',
        description="...",
        url='',
        contact=openapi.Contact(email="doroxincavely@gmail.com"),
        license=openapi.License(name="open"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

start_url = 'api/'

urlpatterns = [
    path(start_url+'admin/', admin.site.urls),
    path(start_url+'api-auth/', include('rest_framework.urls')),

    path(start_url+'main/', include('main.urls')),
    
]

# urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
# urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

if DEBUG:
    urlpatterns += [
        path(start_url+'api-info/', 
             schema_view.with_ui('swagger', cache_timeout=0), 
             name='schema-swagger-ui'),
        path(start_url+'api-info/redoc/', 
             schema_view.with_ui('redoc', cache_timeout=0), 
             name='schema-redoc'),
    ]