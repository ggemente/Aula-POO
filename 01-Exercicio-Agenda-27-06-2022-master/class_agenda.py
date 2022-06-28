#Classe própria para salvar e listar os dados inseridos na class_contato.
from class_contato import *
class Agenda:
    def __init__(self):
        #Atributo do Objeto
        self.listaContatos = []
    #Método: salvar_contatos(self)
    def salvar_contatos(self):
        self.listaContatos.append(Contato())

    def listar_contatos(self):
        for i in range(len(self.listaContatos)):
            print(
                    'Código: ', self.listaContatos[i].cod,
                    'Nome: ', self.listaContatos[i].nome,
                    'Telefone: ', self.listaContatos[i].telefone
            )
    def alterar_contatos_tel(self):
        for i in range(len(self.listaContatos)):
            print('Código: ', self.listaContatos[i].cod,
            'Nome: ', self.listaContatos[i].nome,
            'Telefone: ', self.listaContatos[i].telefone)
        in_cod=input('Insira o código do contato.\n: ')
        for i in range(len(self.listaContatos)):
            if self.listaContatos[i].cod == in_cod:
                self.listaContatos[i].telefone=input('Insira aqui o novo número.\n: ')
                
