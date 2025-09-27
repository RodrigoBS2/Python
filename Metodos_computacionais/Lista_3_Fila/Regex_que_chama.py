class Fila:
    def __init__(self):
        self.fila = []
        
    def inserir (self,Input):
        while len(Input) != 0 :
            self.fila.append(Input.pop(0))
    
    def verificar(self):
        First = self.fila.pop(0)
        Last = self.fila.pop()
        if (First == Last):
            print("VERDADE")
        else:
            print("FALSO")
            
F = Fila()
Input = list(input())
F.inserir(Input)
F.verificar()

