from django.db import models

class venda(models.Model):
    cliente = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        abstract = True