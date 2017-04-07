# #!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# CREATION DATE 07/04/2017

from __future__ import unicode_literals

variaveis = []

nome_programa = input("nome programa ")

caminho = "F:\PRGNEW\%s\FONTES\%s" % (nome_programa[0:2], nome_programa + ".CBL")

with open(caminho, "r") as arq:
    for linha in arq.readlines():
        if linha.__contains__("PIC"):
            if linha.rsplit()[0] != "PIC":
                variaveis.append(linha.rsplit()[1])
    arq.close()

with open("variaveis.xlsx", "a+") as arq:
    for v in variaveis:
        arq.writelines(v+"\n")
    arq.close()