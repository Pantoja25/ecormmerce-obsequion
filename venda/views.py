from django.shortcuts import render, redirect
from .models import Venda
from .forms import VendaForm
from itemVenda.models import ItemVenda

def carrinho(request):
    carrinho = Venda.objects.filter(status=0)
    
    return render(request, 'vendas/carrinho.html', {'carrinho': carrinho})

def adicionarItemCarrinho(request):
    if request.method == "POST":
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('carrinho')