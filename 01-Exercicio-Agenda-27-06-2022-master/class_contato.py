#Classe própria para inserir os dados de cadastro que serão salvos na class_agenda
class Contato:
    #def metodo(argumento1, argumento2 etc.)
    #def __init__(self, cod, nome, telefone):
    #    #ObjetoCriado.atributo = argumentoX
    #    self.cod = cod #Os atributos podem ser passados por entradas também, não obrigatoriamente por argumentos.
    #    self.nome = nome
    #    self.telefone = telefone
    def __init__(self):
        #ObjetoCriado.objeto = argumentoX
        self.cod = input('Digite o Cod: ') #Os atributos podem ser passados por entradas também, não obrigatoriamente por argumentos.
        self.nome = input('Digite o Nome: ')
        self.telefone = input('Digite o Telefone: ')