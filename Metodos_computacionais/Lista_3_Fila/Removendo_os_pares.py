class Fila:
    def __init__(self):
        self.fila = []
        
    def inserir (self,Input):
        while len(Input) != 0 :
            self.fila.append(Input.pop(0))
    
    def remover(self):
        aux = []
        while len(self.fila) != 0:
            num = self.fila.pop(0)
            if (num % 2) != 0:
                aux.append(num)
        self.fila = aux
        
    def printar(self):
        print(self.fila)

F = Fila()
Input = list(map(int,input().split()))
F.inserir(Input)
F.remover()
F.printar()
