def juntar_string(list_string):
  string = ' '.join(list_string)
  return string

def separar_string(string):
  list_string = string.split(' ')    
  return list_string
  
class Node:
    def __init__(self,label,idade):
        self.label = label   
        self.idade = idade
        self.next = None 
    
    def getLabel(self):
        return self.label
        
    def getIdade(self):
        return self.idade

    def getNext(self):
        return self.next

    def setLabel(self,label):
        self.label = label
        
    def setIdade(self,idade):
        self.idade = idade

    def setNext(self,next):
        self.next = next


class SLL:
    def __init__(self):
        self.head = None
        self.len = 0
        
    def add(self, label, idade):    #--------------------> ordem crescente
        if self.search(label) == False:
            node = Node(label, idade)
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
    
    def add_Decrescente(self, label, idade):    #--------------------> ordem decrescente
        if self.search(label) == False:
            node = Node(label, idade)
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
            dado = [self.head.getLabel(), self.head.getIdade()]
            self.head = self.head.getNext()
            return dado
           
    def show(self):
            aux = self.head
            while aux != None:
                print('Idade: {} Nome: {}'.format(aux.getIdade(),aux.getLabel()))
                aux = aux.getNext()
            print()

    def search(self, label):
        aux = self.head
        while aux != None:
            if aux.getLabel() == label:
                return True
            aux = aux.getNext()
        return False

def organizar(dado):
    dado = separar_string(dado)
    idade = int(dado.pop())
    dado = [juntar_string(dado)]
    dado.append(idade)
    return dado
    
# Função principal:

sllA = SLL() #----------> receberá as entradas
copia = SLL()
sllB = SLL() #----------> receberá os dados da copia de ordem inversa
quantidade = int(input())

# Adicionando elementos na primeira lista:

while quantidade != 0:      
    dado = str(input())
    dado = organizar(dado) #-------------------> dado = [Nome, idade]
    sllA.add(dado[0],dado[1])
    quantidade = quantidade - 1

# Adicionando elementos da primeira lista para a segunda:

copia = sllA 
Z = copia.remove() 
while Z != None:
    sllB.add_Decrescente(Z[0],Z[1])
    Z = copia.remove()

# Mostrando os dados na nova lista
sllB.show()    

    
    