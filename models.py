from __future__ import unicode_literals
import peewee

db = peewee.SqliteDatabase("dicionario.db")


class Dicionario(peewee.Model):
    variavel = peewee.CharField(verbose_name="Variavel", max_length=50)
    tamanho = peewee.CharField(verbose_name="Tamanho", max_length=4)
    tipo = peewee.CharField(verbose_name="Tipo Variavel", max_length=20)
    descricao = peewee.TextField(verbose_name="Descrição", null=True)

    class Meta:
        database = db
