#!/usr/bin/python3
# bibgen.py
# Programa que gera referencias bibliograficas em bibLaTeX
# joao_zonzini 26/11/21

import os, sys
import bib_utils

## caso o usuario nao de o caminho para salvar a referencia, cancela
if len(sys.argv) < 2:
    print("Forneça o caminho da bibliografia como argumento da linha de comando.")
    exit(0)

## pega esse caminho como ultimo elemento de argv
salvar_em = sys.argv[-1]

## user vai ao menu e funcao enche as variaveis com o necessario
ref_dict, classe = bib_utils.selecionar_referencia()

## pede do usuario os dados da referencia
ref_dict = bib_utils.pedir_dados(ref_dict)

## concatena todos os dados da referencia em uma string
referencia_criada = bib_utils.concatena_dados(ref_dict, classe)

## por fim, acrescenta a referencia ao caminho dado
bib_utils.salvar_referencia(referencia_criada, salvar_em)
