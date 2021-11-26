#!/usr/bin/python3
# bib_utils.py
# Modulo de funcoes para o programa bibgen.py
# joao_zonzini 26/11/21

import os

def limpar_tela():
    os.system("clear")


def selecionado_artigo():
    print("------|Selecionado: Artigo|------")
    artigo_dict = {
        "label": "",
        "author": "",
        "title": "",
        "subtitle": "",
        "journal": "",
        "volume": "",
        "pages": "",
        "year": ""
    }

    return artigo_dict


def selecionado_livro():
    print("------|Selecionado: Livro|------")
    artigo_dict = {
        "label": "",
        "volume": "",
        "title": "",
        "pagetotal": "",
        "author": "",
        "maintitle": "",
        "year": "",
        "editor": "",
        "editortype": "",
        "edition": "",
        "publisher": "",
        "location": "",
        "series": ""
    }

    return artigo_dict


def menu_tipo_ref():
    print("Opções de referência:")
    print("1 - Livro.")
    print("2 - Livro de vários volumes.")
    print("3 - Artigo.")
    print("4 - Dissertação de mestrado.")
    print("0 - Cancelar e sair.")

    return(int(input("Selecione: ")))

def pedir_dados(ref_dict):
    ## pedindo as infos da referencia
    for i in ref_dict:
        ref_dict[i] = input(f"{i}: ")

    limpar_tela()
    return ref_dict


def concatena_dados(ref_dict, classe):
    referencia_criada = ""
    ## cria o tipo de referencia e depois a label pra comecar a referencia
    referencia_criada = classe + f"{ref_dict['label']},\n"
    for i in ref_dict:
        if i == "label":  ## a label esta incluida no dict, nao queremos que concatene
            pass
        elif ref_dict[i] == "": ## se o campo for vazio, nao concatenar
            pass                ## faz nada
        else:                   ## fora tudo, realmente concatena o campo
            referencia_criada = referencia_criada + f"\t{i}: {ref_dict[i]},\n"

    referencia_criada = referencia_criada + "}\n"

    print(referencia_criada)
    return referencia_criada


def salvar_referencia(referencia_criada, salvar_em):
    arquivo = open(salvar_em, "a")

    arquivo.write(f"\n")
    arquivo.write(referencia_criada)

    arquivo.close()


def selecionar_referencia():
    while True:
        tipo_ref = menu_tipo_ref()
        limpar_tela()

        if tipo_ref == 0:
            print("Você escolheu sair.")
            quit()
        elif tipo_ref == 1:
            ref_dict = selecionado_livro()
            classe = "@book{"
            break
        elif tipo_ref == 2:
            print("Livro de vários volumes em desenvolvimento.")
            break
        elif tipo_ref == 3:
            ref_dict = selecionado_artigo()
            classe = "@article{"
            break
        elif tipo_ref == 4:
            print("Dissertação em desenvolvimento.")
            break
        else:
            print("Opção inválida,tente novamente.")

    return ref_dict, classe
