# receitas/views.py
from django.shortcuts import render, get_object_or_404
from .models import Foto

def galeria_home(request):
    query = request.GET.get('q')
    if query:
        fotos = Foto.objects.filter(titulo__icontains=query)
    else:
        fotos = Foto.objects.all()
    
    return render(request, 'galeria/home.html', {'cards': fotos})

def foto_detalhe(request, id):
    foto = get_object_or_404(Foto, pk=id)
    return render(request, 'galeria/foto_detalhe.html', {'foto': foto})