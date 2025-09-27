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


class SimplyLinkedList:
    def __init__(self):
        self.head = None        # Armazena um Node
        self.len = 0
        
    def add(self, label):
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
        
    def remove(self, label):
        if self.search(label) == True:
            if self.head.getLabel() == label and self.head.getNext() == None:
                self.head = None
            elif self.head.getLabel() == label:
                self.head = self.head.getNext()
            else:
                aux1 = self.head
                aux2 = self.head.getNext()
                while aux2 != None:
                    if aux2.getLabel() == label:
                        #aux1.setNext(aux2.getNext())
                        aux2 = aux2.getNext()
                        aux1.setNext(aux2)
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
            aux = self.head
            while aux != None:
                print(aux.getLabel(), end=' ')
                aux = aux.getNext()
            print()

    def search(self, label):
        aux = self.head
        while aux != None:
            if aux.getLabel() == label:
                return True
            aux = aux.getNext()
        return False
        

sll = SimplyLinkedList()
sll.add(1)
sll.add(2)
sll.add(3)
sll.add(5)
sll.show()

sll.add(0)
sll.show()

sll.add(4)
sll.show()

sll.add(2.5)
sll.show()

sll.alter(2.5,8)
sll.show()
