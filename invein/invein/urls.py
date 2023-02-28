
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from proyectos.views import panel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('panel/', panel, name='panel'),
    path('', include('proyectos.urls')),
]
