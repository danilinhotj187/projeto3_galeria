# galeria/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.galeria_home, name='galeria_home'),
    path('foto/<int:id>/', views.foto_detalhe, name='foto_detalhe'),
]