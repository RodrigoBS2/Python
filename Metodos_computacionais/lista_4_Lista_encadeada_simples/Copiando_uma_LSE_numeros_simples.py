def separar_string(string):
  list_string = string.split(' ')    
  return list_string
  
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
        
    def add(self, label):    #--------------------> ordem crescente
        if self.search(label) == False:
            node = Node(label)
            if self.head == None: # or self.len == 0
                self.head = node
            elif node.getLabel() < self.head.getLabel():
                node.setNext(self.head)
                self.head = node
            else:
                aux1 = self.head
                aux2 = self.head.getNext() 
                flag_insert = False
                while aux2 != None: 
                    if aux2.getLabel() > node.getLabel():
                        flag_insert = True
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
                        
                if flag_insert == True:
                    node.setNext(aux1.getNext())
                    aux1.setNext(node)
                else:
                    aux1.setNext(node)
        else:
            print("Elemento repetido")
    
    def add_Decrescente(self, label):    #--------------------> ordem decrescente
        if self.search(label) == False:
            node = Node(label)
            if self.head == None: # or self.len == 0
                self.head = node
            elif node.getLabel() > self.head.getLabel():
                node.setNext(self.head)
                self.head = node
            else:
                aux1 = self.head
                aux2 = self.head.getNext() 
                flag_insert = False
                while aux2 != None: 
                    if aux2.getLabel() < node.getLabel():
                        flag_insert = True
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
                        
                if flag_insert == True:
                    node.setNext(aux1.getNext())
                    aux1.setNext(node)
                else:
                    aux1.setNext(node)
        else:
            print("Elemento repetido")
        
    def remove(self):
        if self.head == None:
            return None
        else:
            dado = self.head.getLabel()
            self.head = self.head.getNext()
            return dado
           
    def show(self):
            aux = self.head
            while aux != None:
                print(aux.getLabel(), end = ' ' )
                aux = aux.getNext()
            print()

    def search(self, label):
        aux = self.head
        while aux != None:
            if aux.getLabel() == label:
                return True
            aux = aux.getNext()
        return False

def Organizar(dado):
    aux = []
    while len(dado) != 0:
        z = dado.pop()
        if z != '':
            aux.append(int(z))
    return aux
    
    
# Função principal:

sllA = SLL() #----------> receberá as entradas
copia = SLL()
sllB = SLL() #----------> receberá os dados da copia de ordem inversa


# Adicionando elementos na primeira lista:

dado = str(input())
dado = separar_string(dado)#-------------------> dado = lista com alguns dados do tipo '' em vez de, por exemplo, '2'
dado = Organizar(dado) #-----------------------> lista de numeros inteiros

while len(dado)!= 0:
    sllA.add(dado.pop())

# Passando os elementos da copia de ordem invertida:

copia = sllA 
Z = copia.remove() 
while Z != None:
    sllB.add_Decrescente(Z)
    Z = copia.remove()

# Mostrando os dados na nova lista
sllB.show()    

    



    
 