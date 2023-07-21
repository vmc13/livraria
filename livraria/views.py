from django.shortcuts import render, get_object_or_404
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

def detalhar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    return render(request, 'livraria/detalhar_livro.html', {'livro':livro})

# video 14