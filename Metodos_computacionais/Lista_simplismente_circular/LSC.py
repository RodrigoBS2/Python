class Node:
  def __init__(self,rg, label, ipa):
    self.label = label 
    self.rg = rg
    self.ipa = ipa
    self.next = None

  def getLabel(self):
    return self.label

  def getrg(self):
    return self.rg

  def getipa(self):
    return self.ipa

  def getNext(self):
    return self.next
    
  def setLabel(self, label):
    self.label = label

  def setrg(self, rg):
    self.rg = rg

  def setipa(self, ipa):
    self.ipa = ipa

  def setNext(self, next):
    self.next = next

class CircularLinkedList:
  def __init__(self):
    self.head = None
    self.len = 0

  # insert
  def insertSorted(self, rg, label, ipa):
    aux = self.head
    i = 0
    while i < self.getLength():
      if aux.getLabel() > label: # inserir em ordem crescente
        break
      aux = aux.getNext()
      i+=1
    if i == self.getLength() and i!=0:
      self.append(rg, label, ipa)
    else:
      self.insert(rg, label, ipa, i)

  def append(self, rg, label, ipa):
    self.insert(rg, label, ipa,self.getLength())

  def insert(self, rg, label, ipa, index):
    if index <= self.getLength() and index >= -(self.getLength()+1) and self.search(label) == None:
      node = Node(rg, label, ipa)
      if index < 0:
        index = self.getLength() + index + 1

      if self.empty() == True:
        self.head = node
        node.setNext(node) #self.head.setNext(self.head)
        self.len += 1
        return
      # Pego o bloco anterior ao bloco que quero adicionar, se o primeiro 
      # nodo (index == 0) for a posição selecionada, é preciso mover o before 
      # até a última posição para manter o ciclo
      aux = self.head
      for _ in range(self.getLength() - 1 if index == 0 else index - 1):
        aux = aux.getNext()
      node.setNext(aux.getNext())
      aux.setNext(node)
      if index == 0:
        self.head = node
      self.len += 1  

  # remove
  def removeLabel(self, label):
    index = self.search(label)
    if index != None:
      self.removeIndex(index)

  def removeIndex(self, index):
    # Se meu index for maior que o tamanho da minha lista ou negativo (ERRO!)
    if (index >= self.len):
        print(f"Index out of range: {index}, size: {self.len}")
        return
    
    # Se o tamanho da minha lista for 1, reseta a lista
    if self.len == 1:
        self.head = None
        self.len = 0
        return
    
    # Remover um valor em um index dentro do intervalo:

    # Pego o bloco anterior e o próximo do bloco que quero remover, se o primeiro 
    # nodo (index == 0) for removido, é preciso mover o before até a última 
    #posição para manter o ciclo
    before = self.head
    for _ in range(self.len - 1 if index == 0 else index - 1):
        before = before.next
    after = before.next.next
    
    # Faço meu bloco anterior receber como próximo, o bloco depois do que quero remover
    # Dessa forma perco a informação do bloco no índice que quero remover
    before.next = after

    # Se meu index for 0, também preciso alterar a cabeça da minha lista
    # fazendo com que ela seja agora o bloco que vinha logo depois do que eu queria remover
    if(index == 0):
        self.head = after
    
    #Diminuo um do tamanho da minha lista
    self.len -= 1
    return

  # search
  def search(self, label):
    aux = self.head
    for i in range(self.getLength()):
      if aux.getLabel() == label:
        return i
      aux = aux.getNext()  
    return None

  # show
  def show(self):
    if self.empty() != True: # not self.empty() #self.empty() != True
      print(self.head.getrg(),self.head.getLabel(),self.head.getipa())    
      aux = self.head.getNext()
      while aux != self.head: # for i in range(self.getLength()):
        print(aux.getrg(),aux.getLabel(),aux.getipa()) 
        aux = aux.getNext()   
      print()        

  # aux_methods
  def getLength(self):
    return self.len
  
  def empty(self):
    if self.getLength() == 0:
      return True
    return False



cll = CircularLinkedList()

cll.insertSorted('C','a','q')
cll.insertSorted('F','e','r')
cll.insertSorted('J','f','g')
cll.insertSorted('M','c','x')

cll.insertSorted('O','z','a')
cll.insertSorted('A','k','l')
cll.show()


