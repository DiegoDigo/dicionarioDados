# #!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# CREATION DATE 07/04/2017
from __future__ import unicode_literals

from builtins import print

from models import Dicionario as dicionario
import peewee


if __name__ == '__main__':
    try:
        dicionario.create_table()
    except peewee.OperationalError:
        print('Tabela Dicionario ja existe!')


variavel = ""
tipo = ""
tamanho = ""
descricao = ""

nome_programa = input("nome programa ")

caminho = "F:\PRGNEW\%s\BOK\%s" % (nome_programa[0:2], nome_programa + ".EFDE")

arq = open(caminho, "rb")
for linha in arq.readlines():
    linha = str(linha)
    if linha.__contains__("PIC") and not linha.__contains__("REDEFINES") \
            and not linha.__contains__("===>") and not linha.__contains__("FILLER"):
        if linha.rsplit()[0] != "PIC" and len(linha.rsplit()) >= 5:
            variavel = linha.rsplit()[2].replace("'", "")
            tamanho = linha.rsplit()[4][2:5]
            if linha.rsplit()[4][0] == "X" or linha.rsplit()[4][0] == "x":
                tipo = "Alfanumerico"
            else:
                tipo = "Numerico"
        dicionario.create(variavel=variavel, tamanho=tamanho, tipo=tipo, descricao=descricao)
arq.close()