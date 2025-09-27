class Stack:
  def __init__(self):
    self.stack = []           # Declaração de uma lista

  def push(self, e):
    self.stack.append(e)      # "self.stack.append('valor')" adiciona um elemento na lista self.stack

  def pop(self):
    return self.stack.pop()  # "self.stack.pop()" retira o elemnto q está no topo da lista e o retorna 

  def top(self):
    if len(self.stack) == 0:  # "len(self.stack)" diz o tamanho da lista
      return None
    else:
      return self.stack[-1]   # "self.stack[-1]" retorna o valor do ultimo elemento da lista

  def show(self):
    for i in self.stack:
      print(i, end=' ')
    print()
    #print(self.stack)

  def inverter(self):
    aux = Stack()
    while self.top() != None:
      aux.push(self.pop())
      aux.show() 
    self.stack = aux.stack
    print()
    self.show()
    
    

