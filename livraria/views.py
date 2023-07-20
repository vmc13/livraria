from django.shortcuts import render
from livraria.models import Autor, Categoria, Livro


def listar_autores(request):
    autores = Autor.objects.all()

    return render(request, 'livraria/listar_autores.html', {'autores':autores})

def listar_categorias(request):
    categorias = Categoria.objects.all()

    return render(request, 'livraria/listar_categorias.html', {'categorias':categorias})

def listar_livros(request):
    livros = Livro.objects.all()

    return render(request, 'livraria/listar_livros.html', {'livros':livros})