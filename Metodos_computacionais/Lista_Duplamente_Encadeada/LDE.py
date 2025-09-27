class Node:
    def __init__(self,label):
        self.label = label   
        self.next = None 
        self.prev = None
    
    def getLabel(self):
        return self.label

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setLabel(self,label):
        self.label = label

    def setNext(self,next):
        self.next = next
    
    def setPrev(self,prev):
        self.prev = prev


class SimplyLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
        
    def add(self, label):
        if self.search(label) == False:
            node = Node(label)
            
            if self.head == None: # or self.len == 0
                self.head = node
            elif node.getLabel() < self.head.getLabel():
                node.setNext(self.head)
                self.head.setPrev(node)
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
                    node.setPrev(aux1)
                    aux1.setNext(node)
                    aux2.setPrev(node)
                else:
                    aux1.setNext(node)
                    aux1.getNext().setPrev(aux1)
        else:
            print("Elemento repetido")
        
    def remove(self, label):
        if self.search(label) == True:
            if self.head.getLabel() == label and self.head.getNext() == None:
                self.head = None
            elif self.head.getLabel() == label:
                self.head = self.head.getNext()
                self.head.setPrev(None)
            else:
                aux1 = self.head
                aux2 = self.head.getNext()
                while aux2 != None:
                    if aux2.getLabel() == label:
                        #aux1.setNext(aux2.getNext())
                        aux2 = aux2.getNext()
                        aux1.setNext(aux2)
                        if aux2 != None:
                            aux2.setPrev(aux1)
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()

    def alter(self,old,new):
        exist_old = self.search(old)
        exist_new = self.search(new)
        if exist_old == True and exist_new == False:
            self.remove(old)
            self.add(new)

    def show(self):
        if self.head != None:
            aux = self.head
            while aux.getNext() != None:
                print(aux.getLabel(), end=' ')
                aux = aux.getNext()
            print(aux.getLabel(), end=' // ')
            #do fim para o começo
            while aux.getPrev() != None:
                print(aux.getLabel(), end=' ')
                aux = aux.getPrev()
            print(aux.getLabel())
            

    def search(self, label):
        aux = self.head
        while aux != None:
            if aux.getLabel() == label:
                return True
            aux = aux.getNext()
        return False
        
sll = SimplyLinkedList()

sll.add(1)
sll.add(0)
sll.add(2)
sll.add(3)
sll.add(5)

sll.show()

sll.add(4)

sll.show()

sll.remove(3)
sll.show()

sll.alter(4,7)
sll.show()