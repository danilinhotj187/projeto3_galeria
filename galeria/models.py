from django.db import models

# Classe base (abstrata)
class Midia(models.Model):
    titulo = models.CharField(max_length=150, null=False, blank=False)
    legenda = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        abstract = True  # não cria tabela no banco, só serve de base

    def __str__(self):
        return self.titulo


# Classe Foto herdando de Midia
class Foto(Midia):
    imagem = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)


# Outra classe herdando de Midia (exemplo)
class Video(Midia):
    arquivo = models.FileField(upload_to='videos/%Y/%m/%d/')
    duracao = models.DurationField(null=True, blank=True)
