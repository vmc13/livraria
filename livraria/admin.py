from django.contrib import admin

# Register your models here.
from .models import Categoria, Autor, Livro

admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Livro)