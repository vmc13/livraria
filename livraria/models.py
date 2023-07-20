from django.db import models
from django.conf import settings

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    nome = models.CharField(max_length=200)
    autor = models.ManyToManyField(Autor, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    codigo = models.CharField(max_length=20)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    imagem = models.ImageField(upload_to='livraria/media', blank=True)
    ano = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome
