from django.urls import path
from . import views

urlpatterns = [
    path('', views.galeria_home, name='galeria_home'),
    path('foto/<int:id>/', views.foto_detalhe, name='foto_detalhe'),

    # se quiser usar vídeos também:
    path('videos/', views.video_home, name='video_home'),
    path('video/<int:id>/', views.video_detalhe, name='video_detalhe'),
]
