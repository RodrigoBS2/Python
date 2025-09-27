class Fila:
    def __init__(self):
        self.fila = []
    
    def inserir (self,Input):
        while len(Input) != 0 :
            self.fila.append(Input.pop(0))
    
    def verificar(self):
        aux = self.fila
        x = 0                   # Receberá a quantidade de "("  
        y = 0                   # Receberá a quantidade de ")" 
        
        while len(aux) != 0:    # Adicionando os '(' e ')' em x e y respectivamente
            z = aux.pop(0)
            if z == '(':
                x = x + 1
            if z == ')':
                y = y + 1
                
        # Comparando as quantidades x e y 
        if x > y:
            print('ERRADO: Abre parênteses sem o fecha parênteses correspondente')
        elif x < y:
            print('ERRADO: Fecha um parênteses sem ter aberto')
        else:
            print('CERTO')

F = Fila()
Input = list(input())
F.inserir(Input)
F.verificar()