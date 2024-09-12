from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['valor','datahora','nome_vendedor','nome_fabricante','quantidade_vendida','nome','cliente','adm',]
