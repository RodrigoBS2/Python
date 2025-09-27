def join_string(list_string):             #------->  Juntar strings
    string = ' '.join(list_string)
    return string

def split_string(string):               #---------> Separar strings
    list_string = string.split(' ')    
    return list_string

def organizar(Entrada):
    z = Entrada.pop(0)
    aux = []
    while len(Entrada) != 0:
        aux.append(Entrada.pop())
    aux = join_string(aux)
    aux = [aux]
    aux.insert(0,z)
    return aux
  
  
class Node:
    def __init__(self,label,prio):
        self.label = label 
        self.prio = prio
        self.next = None 
        self.prev = None
    
    def getLabel(self):
        return self.label
    
    def getPrio(self):
        return self.prio

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setLabel(self,label):
        self.label = label

    def setPrio(self,prio):
        self.prio = prio

    def setNext(self,next):
        self.next = next
    
    def setPrev(self,prev):
        self.prev = prev
        
class DLL:
    def __init__(self):
        self.head = None
        self.len = 0
        
    def add(self, label, prio):
        if self.search(label) == False:
            node = Node(label,prio)
            
            if self.head == None: # or self.len == 0
                self.head = node
                return True
            elif node.getPrio() > self.head.getPrio():
                node.setNext(self.head)
                self.head.setPrev(node)
                self.head = node
                return True
            else:
                aux1 = self.head
                aux2 = self.head.getNext() 
                flag_insert = False
                while aux2 != None: 
                    if aux2.getPrio() < node.getPrio():
                        flag_insert = True
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
                        
                if flag_insert == True:
                    node.setNext(aux1.getNext())
                    node.setPrev(aux1)
                    aux1.setNext(node)
                    aux2.setPrev(node)
                    return True
                else:
                    aux1.setNext(node)
                    aux1.getNext().setPrev(aux1)
                    return True
        else:
            return False
        
    def remove(self, label):
        if self.search(label) == True:
            if self.head.getLabel() == label and self.head.getNext() == None:
                self.head = None
                return True
            elif self.head.getLabel() == label:
                self.head = self.head.getNext()
                self.head.setPrev(None)
                return True
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
                        return True
                        break
                    aux1 = aux1.getNext()
                    aux2 = aux2.getNext()
    
    def Realizar_Tarefa(self):
        if self.head.getLabel() == None and self.head.getNext() == None:
            self.head = None
        else:
            self.head = self.head.getNext()
            self.head.setPrev(None)
        return True
    
    def tarefa_dependente(self,label):
        if self.head != None:
            quantidade = 0
            aux = self.head
            while aux.getNext() != None:
                if aux.getLabel != label:
                    quantidade = quantidade + 1
                else:
                    break
                aux = aux.getNext()
            print('serão executadas {} tarefas antes da informada'.format(quantidade))
        
    
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
                print('Descricao: {}, Prioridade: {}'.format(aux.getLabel(),aux.getPrio()))
                aux = aux.getNext()
            print('Descricao: {}, Prioridade: {}'.format(aux.getLabel(),aux.getPrio()))
    
    def show_Prio(self,prio):           #--------> E
        if self.head != None:
            aux = self.head
            verificador = False
            while aux.getNext() != None:
                if aux.getPrio() == prio:
                    print('Descricao: {}'.format(aux.getLabel()))
                    verificador = True
                aux = aux.getNext()
            
            if aux.getPrio() == prio:
                print('Descricao: {}'.format(aux.getLabel()))
                verificador = True
            if verificador == False:
                print("nenhuma tarefa como esse prioridade foi encontrada")
            

    def search(self, label):
        aux = self.head
        while aux != None:
            if aux.getLabel() == label:
                return True
            aux = aux.getNext()
        return False
        
dll = DLL()
E = input()
E = split_string(E) #--------> E = ['Letra', 'tarefa' , 'prioridade']


while E[0] != 'H':
    if E[0] == 'C':                     #-----------------> Realizar uma tarefa
       if dll.Realizar_Tarefa() == True:
           print('Tarefa executada')
    
    elif E[0] == 'F':       #----------------> Mostrar todas as tarefas
        dll.show()
    
    elif E[0] == 'A':               #----------------------> Adicionar tarefa
        if int(E[2]) > 0 and int(E[2]) < 11:
            if dll.add(E[1],int(E[2])) == True:
                print('tarefa adicionada com sucesso')
            else:
                print('já tem uma atividade com essa descrição')
        else:
            print('tarefa não inserida por não ter prioridade válida')
    
    elif E[0] == 'B':   #------> E = [letra, tarefa]
        dll.tarefa_pendente(E[1])
    
    elif E[0] == 'D':       #--------------------> Remover tarefa
        if dll.remove(E[1]) == True:
            print('Tarefa removida')
    
    elif E[0] == 'E':           #----------------> E = [letra, prioridade] #----------------> Mostrar as tarejas de tal prioridade
        if int(E[1]) > 0 and int(E[1]) < 11:
            dll.show_Prio(int(E[1]))
    
    else:   #---> Z[0] == 'G'    #----------------> Alterar prioridade da tarefa
        if int(E[2]) > 0 and int(E[2]) < 11:
            if dll.remove(E[1]) == True:
                if dll.add(E[1],int(E[2])) == True:
                    print('tarefa alterada com sucesso')
        else:
            print('tarefa não alterada por não ter prioridade válida')
    
    E = input()
    E = split_string(E)

print('programa encerrado')  
    