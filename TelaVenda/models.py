from django.db import models

class Venda(models.Model):
    cliente = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    data = models.DateTimeField()

    def __str__(self):
        return f"{self.cliente} comprou {self.quantidade} de {self.produto} em {self.data}"
