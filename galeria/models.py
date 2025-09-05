# galeria/models.py
from django.db import models

class Foto(models.Model):
    titulo = models.CharField(max_length=150, null=False, blank=False)
    legenda = models.CharField(max_length=255, null=False, blank=False)
    imagem = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.titulo