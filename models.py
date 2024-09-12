# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Classe(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classe'


class Endereo(models.Model):
    id_endereco = models.IntegerField(db_column='ID Endereco', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rua = models.CharField(db_column='Rua', max_length=50, blank=True, null=True)  # Field name made lowercase.
    número = models.IntegerField(db_column='Número', blank=True, null=True)  # Field name made lowercase.
    completo = models.CharField(db_column='Completo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    país = models.CharField(db_column='País', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='Cep', max_length=10, blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endereço'


class ItemVenda(models.Model):
    id_venda = models.OneToOneField('Venda', models.DO_NOTHING, db_column='id_venda', primary_key=True)
    id_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='id_produto', blank=True, null=True)
    preco = models.FloatField(blank=True, null=True)
    qtd_vendida = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_venda'


class Produto(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data_validade = models.DateField(db_column='DATA_VALIDADE', blank=True, null=True)  # Field name made lowercase.
    nome_fornecedor = models.CharField(db_column='NOME_FORNECEDOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    em_desconto = models.IntegerField(db_column='EM_DESCONTO', blank=True, null=True)  # Field name made lowercase.
    preco_desconto = models.FloatField(db_column='PRECO_DESCONTO', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='PRECO', blank=True, null=True)  # Field name made lowercase.
    qtd_estoque = models.IntegerField(db_column='QTD_ESTOQUE', blank=True, null=True)  # Field name made lowercase.
    classe = models.ForeignKey(Classe, models.DO_NOTHING, db_column='CLASSE_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produto'


class Rastreamento(models.Model):
    id_produto_i = models.IntegerField(db_column='ID_Produto I', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    distribuidora = models.CharField(db_column='Distribuidora', max_length=50, blank=True, null=True)  # Field name made lowercase.
    data_envio = models.DateTimeField(db_column='Data_Envio', blank=True, null=True)  # Field name made lowercase.
    data_entrega_estimada = models.DateTimeField(db_column='Data_Entrega_Estimada', blank=True, null=True)  # Field name made lowercase.
    rastreamento = models.CharField(db_column='Rastreamento', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rastreamento'


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefone = models.IntegerField(db_column='Telefone', blank=True, null=True)  # Field name made lowercase.
    funcao = models.IntegerField(db_column='Funcao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'


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
