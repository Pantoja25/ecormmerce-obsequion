from django.db import models
#
#class Venda(models.Model):
#    cliente = models.CharField(max_length=100)
#    produto = models.CharField(max_length=100)
#    quantidade = models.IntegerField()
#    preco = models.DecimalField(max_digits=5, decimal_places=2)
#    status = models.IntegerField()
    
    #class Meta:
    #    abstract = True

#class VendaOnline(VendaBase):
#    data_entrega = models.DateField()
#
#class VendaLoja(VendaBase):
#    vendedor = models.CharField(max_length=100)
#


class Venda(models.Model):
    id = models.IntegerField(primary_key=True)
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    datahora = models.DateTimeField(db_column='DataHora', blank=True, null=True)  # Field name made lowercase.
    nome_vendedor = models.CharField(db_column='Nome_Vendedor', max_length=35, blank=True, null=True)  # Field name made lowercase.
    nome_fabricante = models.CharField(db_column='Nome_Fabricante', max_length=50, blank=True, null=True)  # Field name made lowercase.
    quantidade_vendida = models.IntegerField(db_column='Quantidade_Vendida', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=35, blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='Cliente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venda'
