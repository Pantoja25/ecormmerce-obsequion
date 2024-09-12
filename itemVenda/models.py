from django.db import models
#
#class ItemVenda(models.Model):
#    venda = models.ForeignKey(
#        "venda.venda",
#        on_delete=models.CASCADE,
#    )
#
#    qtdVenda = models.IntegerField()
#    precoUND = models.DecimalField(decimal_places=2, max_digits=5)
#    produto = models.IntegerField()
#
    #class Meta:
    #    abstract = True    
    
class ItemVenda(models.Model):
    id_venda = models.ForeignKey('venda.Venda', on_delete=models.CASCADE, db_column='id_venda')
    #id_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='id_produto', blank=True, null=True)
    preco = models.FloatField(blank=True, null=True)
    qtd_vendida = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_venda'


