from django.shortcuts import render, redirect
from .models import Venda
from .forms import VendaForm
from itemVenda.models import ItemVenda

def carrinho(request):
    carrinho = Venda.objects.filter(status=0)
    
    return render(request, 'vendas/carrinho.html', {'carrinho': carrinho})

def adicionarItemCarrinho(request):
    if request.method == "POST":
        venda=Venda.objects.filter(status=1)
        
        if venda:
            itemVenda =  ItemVenda()
            itemVenda.id_venda = venda
            itemVenda.qtd_vendida = request.POST.get("qtd_vendida")
            itemVenda.preco = request.POST.get("preco")
            
            itemVenda.save()
            
            form = VendaForm(request.POST)
            if form.is_valid():
                form.save()
            
        else:
            venda = Venda()
        
    return redirect('carrinho')