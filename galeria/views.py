from django.shortcuts import render, get_object_or_404
from .models import Foto, Video

# Função genérica de listagem
def listar_midia(request, model, template, context_name="items"):
    query = request.GET.get('q')
    if query:
        objetos = model.objects.filter(titulo__icontains=query)
    else:
        objetos = model.objects.all()
    return render(request, template, {context_name: objetos})

# Função genérica de detalhe
def detalhe_midia(request, model, template, context_name="item", pk=None):
    objeto = get_object_or_404(model, pk=pk)
    return render(request, template, {context_name: objeto})

# --- Views específicas ---
def galeria_home(request):
    return listar_midia(request, Foto, 'galeria/home.html', 'cards')

def foto_detalhe(request, id):
    return detalhe_midia(request, Foto, 'galeria/foto_detalhe.html', 'foto', pk=id)

def video_home(request):
    return listar_midia(request, Video, 'galeria/videos.html', 'videos')

def video_detalhe(request, id):
    return detalhe_midia(request, Video, 'galeria/video_detalhe.html', 'video', pk=id)
