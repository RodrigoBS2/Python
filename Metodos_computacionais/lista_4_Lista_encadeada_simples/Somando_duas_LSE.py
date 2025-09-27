class Node:
    def __init__(self,label):
        self.label = label   
        self.next = None 
    
    def getLabel(self):
        return self.label

    def getNext(self):
        return self.next

    def setLabel(self,label):
        self.label = label

    def setNext(self,next):
        self.next = next


class SLL:
    def __init__(self):
        self.head = None
        self.len = 0
        
    def add(self, label):
        if self.search(label) == False:
            node = Node(label)
            if self.head == None: # or self.len == 0
                self.head = node
                self.len = 1
            else:
                aux1 = self.head
                aux2 = self.head.getNext()
                self.len = self.len + 1
                
                while aux2 != None: 
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
                aux1.setNext(node)
        
    def show(self):
            aux = self.head
            while aux != None:
                print(aux.getLabel(), end=' ')
                aux = aux.getNext()
            print()
    
    def pegar_elemento(self):               #-----> Remove o primeiro elemento da lista
        z = self.head.getLabel()
        self.head = self.head.getNext()
        return z
    
    def Tamanho(self):                      #------> Obtem o tamanho da fila
        return self.len
    
    def search(self, label):
        aux = self.head
        while aux != None:
            if aux.getLabel() == label:
                return True
            aux = aux.getNext()
        return False

def adicionar(SLL):     #------> Adicionando os elementos na lista
    quantidade = int(input())
    lista = list(map(int, input().split()))
    for i in range(0,quantidade):
        SLL.add(lista.pop(0))
    



slla = SLL() 
sllb = SLL()

adicionar(slla)
adicionar(sllb)

A = slla.Tamanho()
B = sllb.Tamanho()

sllc = SLL()


while A != 0 or B != 0:         # Adicioando a soma dos elementos de duas lista (slla e sllb) numa terceira lista (sllc)
    if A == 0:
        sllc.add(sllb.pegar_elemento())
        B = B - 1
    
    elif B == 0:
        sllc.add(slla.pegar_elemento())
        A = A - 1
    
    else:
        sllc.add(slla.pegar_elemento() + sllb.pegar_elemento())
        A = A - 1
        B = B - 1
        
sllc.show()      
    