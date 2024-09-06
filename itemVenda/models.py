from django.db import models

class ItemVenda(models.Model):
    venda = models.ForeignKey(
        "Venda",
        on_delete=models.CASCADE,
    )

    qtdVenda = models.IntegerField()
    precoUND = models.DecimalField(decimal_places=2, max_digits=5)
    produto = models.IntegerField()

    class Meta:
        abstract = True    

