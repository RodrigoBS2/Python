class Fila:
    def __init__(self):
        self.fila = []
    
    def inserir (self,Input):
        while len(Input) != 0 :
            self.fila.append(Input.pop(0))
        
    def multi(self):
        aux3 = []
        aux5 = []
        aux = []
        while len(self.fila) != 0 :
            x = self.fila.pop(0)
            if (x % 3) == 0:
                aux3.append(x)
            if (x % 5) == 0:
                aux5.append(x)    
            if ((x % 3) != 0) and ((x % 5) != 0):
                aux.append(x)
        print(aux3)
        print(aux5)
        print(aux)

Num = Fila()
Input = list(map(int,input().split()))
Num.inserir(Input)
Num.multi()

