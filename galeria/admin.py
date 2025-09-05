# galeria/admin.py
from django.contrib import admin
from .models import Foto

class FotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)

admin.site.register(Foto, FotoAdmin)