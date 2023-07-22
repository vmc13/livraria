from django import forms

from livraria.models import Livro

class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = ('nome','autor','categoria','codigo', 
        'quantidade', 'valor', 'imagem', 'ano', 'descricao')

        widgets = {
            'nome': forms.TextInput(attrs={
                 'class': 'form-control',
                 'placeholder':'Ex.: Redes de Computadores'
            }),
            'autor': forms.SelectMultiple(attrs={ 
                'class': 'form-control'
            }),
            'categoria': forms.Select(attrs={ 
                'class': 'form-control'
            }),
            'codigo': forms.TextInput(attrs={ 
                'class': 'form-control',
                'placeholder':'Ex.: 1012'
            }),
            'quantidade': forms.NumberInput(attrs={ 
                'class': 'form-control',
                'placeholder':'Ex.: 40'
            }),
            'valor': forms.NumberInput(attrs={ 
                'class': 'form-control',
                'placeholder':'Ex.: 59,80'
            }),
            'imagem': forms.FileInput(attrs={ 
                'class': 'form-control'
            }),
            'ano': forms.TextInput(attrs={ 
                'class': 'form-control',
                'placeholder':'Ex.: 2019'
            }),
            'descricao': forms.Textarea(attrs={ 
                'class': 'form-control',
                'placeholder':'Ex.: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sagittis a erat ut vulputate. Vestibulum feugiat fermentum efficitur. Duis lacinia orci in auctor luctus. Pellentesque et turpis scelerisque nibh mollis volutpat at ut lacus. Morbi ullamcorper ipsum nisl, sit amet tincidunt augue tincidunt a. Duis at turpis eu purus tincidunt finibus eu sed mi. Maecenas finibus ipsum sed magna pellentesque consequat. Vivamus ac enim ut nisl dictum volutpat porttitor et sem. Nulla facilisi.'
            }),
        }