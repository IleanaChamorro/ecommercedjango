from django.urls import path

from ProjectEcomApp import views
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('tienda/', views.tienda, name="tienda"),
]

#Agregado archivos media
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)