from django.urls import path

from ProjectEcomApp import views
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('servicios/', views.servicios, name="servicios"),
    path('tienda/', views.tienda, name="tienda"),
    path('info/', views.info, name="info"),
    path('contacto/', views.contacto, name="contacto"),
]

#Agregado archivos 
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)