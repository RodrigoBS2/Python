class Pilha:
    def __init__(self):             # Criação da pilha
        self.pilha = []
    
    def inserir(self,Input):
        while len(Input) != 0:
            self.pilha.append(Input.pop())
        
    def inteiro(self):                                 # Metodo para inserir os valores e transformá-los em números inteiros
        aux = []                                       # Foi criado uma lista auxiliar para receber os todos os valores em forma de inteiros
        while len(self.pilha) != 0:
            aux.append(int(self.pilha.pop()))
        self.pilha = aux                               # Após o ciclo while a lista "self.pilha" está vazia. Logo ela irá receber todos os valores inteiros da lista auxiliar e será printada na tela
        return print(self.pilha)
    
    def Produto_soma(self):                            # Função para somar todos os pares e ímpares e multiplica-los 
        par = impar = 0
        while len(self.pilha) != 0:                    # O ciclo while servirá para remover cada elemento da lista a cada repetição 
            numero = self.pilha.pop()                  # A variavel numero irá receber cada elemento da pilha 
            if (numero%2) == 0:                 # O if e o else servirá para identificar se "numero" é par ou impar e adicioná-lo na variavel "par" ou "impar"
                par = par + numero              # A cada repetição a variavel "par" ou "impar" será somada por um novo elemento até que não exista mais elementos na lista
            else:
                impar = impar + numero
        return print(impar * (-par))                   # retornará o produto entre "-(par)" e "impar"
    
    def Printar_Pilha_Vazia(self):
        print(self.pilha)


P = Pilha()
Input = list(map(float, input().split()))
P.inserir(Input)
P.inteiro()
P.Produto_soma()
P.Printar_Pilha_Vazia()