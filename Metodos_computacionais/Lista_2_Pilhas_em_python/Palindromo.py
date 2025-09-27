class Pilha:
    def __init__(self):    #------------------------------------> Criando uma classe "Pilha" para armazenar os valroes e uma lista
        self.pilha = [] 
    
    def enxugar(self):     #------------------------------------> O método "enxugar" irá eliminar todos os elementos que contem ' ' da lista self.pilha
        aux = []                                                # A variável "aux" receberar todos os elementos que não contem ' ' e depois do ciclo será armazenado na self.pilha
        while len(self.pilha) !=0:
            elemento = self.pilha.pop()
            if elemento >= '0':                            # Analisando a tabela ASCII os caracteres de letras maiúsculas e minúsculas tem valores decimais maiores do que o valor decimal do caractere ' '
                aux.append(elemento)
        self.pilha = aux
        
    def minuscula(self):   #------------------------------------> O método "minuscula" passará todos os elementos da lista em letras minúsculas
        aux = str()                                             # A variavel "aux" será usada para concatenar todos os elementos da lista no ciclo while 
        while len(self.pilha) != 0:
            aux = aux + self.pilha.pop() 
        aux = aux.lower()                                       # Após o ciclo while, "aux" recebe o comando "lower()"" para se tornar uma string com caracteres minúsculos 
        self.pilha = list(aux)                                  # A variavel "aux" passará a ser uma lista em "list()"" e será armazenada na pilha self.pilha

    def verificar(self):   #------------------------------------> O método "verificar" irá analisar se a lista é um palíndromo ou não retornando "True" ou "False"
        aux1 = []
        aux2 = []
        
        while len(self.pilha) != 0:                             # Adicionando todos os elemntos de self.pilha em axu1 e aux2 para depois manipular essas pilhas auxiliares
            z = self.pilha.pop()
            aux1.append(z)
            aux2.append(z)
            
        while len(aux1) != 0:                                   # "self.pilha" receberá todos os elementos na ordem inversa para depois ser comparado com a pilha "aux2"
            self.pilha.append(aux1.pop())
            
        while len(self.pilha) != 0:                             # Comparando "self.pilha" com aux2
            if self.pilha.pop() != aux2.pop():
                return print('False')
            return print('True')
            

L = Pilha()
L.pilha = list(input())

L.enxugar()
L.minuscula()
L.verificar()
