from django.db import models

class Venda(models.Model):
    cliente = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(max_length=100)
    
    class Meta:
        abstract = True

#class VendaOnline(VendaBase):
#    data_entrega = models.DateField()
#
#class VendaLoja(VendaBase):
#    vendedor = models.CharField(max_length=100)
#