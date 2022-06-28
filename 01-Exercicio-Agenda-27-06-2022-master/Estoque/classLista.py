from classProduto import *

class Lista:
     def __init__(self):
         self.listaProdutos = []

     def salvar_produtos(self):
         self.listaProdutos.append(Produto())

     def listar_produtos(self):
         for i in range(len(self.listaProdutos)):
             print(
                    'Código: ', self.listaProdutos[i].cod,
                    'Descrição: ', self.listaProdutos[i].desc,
                    'Fabricante: ', self.listaProdutos[i].fab,
                    'Quantidade: ', self.listaProdutos[i].quant
                  )
     def alterar_desc_prod(self):
        for i in range(len(self.listaProdutos)):
            print(
                'Código: ', self.listaProdutos[i].cod,
                'Descrição: ', self.listaProdutos[i].desc,
                'Fabricante: ', self.listaProdutos[i].fab,
                'Quantidade: ', self.listaProdutos[i].quant
                )
        in_cod=input('Insira o código do Produto.\n: ')
        for i in range(len(self.listaProdutos)):
            if self.listaProdutos[i].cod == in_cod:
                self.listaProdutos[i].desc=input('Insira aqui a nova descrição.\n: ')