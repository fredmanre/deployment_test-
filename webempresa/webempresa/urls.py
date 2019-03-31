"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# para los arhicvos estaticos y medias
from django.conf import settings

urlpatterns = [
    # path para el core
    path('', include('core.urls')),
    # path para services
    path('services/', include('services.urls')),
    # para el blog
    path('blog/', include('blog.urls')),
    # path para pages(sample)
    path('page/', include('pages.urls')),
    # para para contacto
    path('contact/', include('contact.urls')),
    # path para el amdin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # para servir ficheros estáticos en desarrollo(para los media)
    from django.conf.urls.static import static
    # ruta a donde buscar los archivos media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# custom titles for admin
admin.site.site_header = 'La Caffetiere'
admin.site.index_title = 'Panel de administracion'
admin.site.site_title = 'La cafetier'
