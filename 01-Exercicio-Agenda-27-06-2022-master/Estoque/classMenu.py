from classLista import *

class Menu:
    def __init__(self):
        lista = Lista()
        while True:
            entrada=input(('1 - Novo Cadastro\n2 - Listar Produtos\n3- Alterar Desc.:\n0 - Sair\n: '))
            if entrada == '1':
                lista.salvar_produtos()
                pass
            elif entrada == '2':
                lista.listar_produtos()
                pass
            elif entrada == '3':
                lista.alterar_desc_prod()
                break
            else:
                print('Opção Inválida')
