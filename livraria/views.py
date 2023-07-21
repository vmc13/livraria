from django.shortcuts import render, get_object_or_404, redirect
from livraria.models import Autor, Categoria, Livro
from livraria.forms import LivroForm


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

def cadastrar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            livro = form.save(commit=False)
            form.save()
            return redirect('detalhar_livro', id=livro.id)
    else:
        form = LivroForm()
    return render(request, 'livraria/editar_livro.html', {'form': form})

def editar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            livro = form.save(commit=False)
            form.save()
            return redirect('detalhar_livro', id=livro.id)
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livraria/editar_livro.html', {'form': form})

