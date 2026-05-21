class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,e):
        print(f"Adicionando o elemento {e} na fila")
        self.queue.append(e)
    def dequeue(self):
        if len(self.queue) == 0:
            print('Fila vazia')
        else:
            print("Retirando elemento da fila")
            self.queue.pop(0)
    def front(self):
        return self.queue[0]
    def show(self):
        print(f"Os elementos da fila são: {self.queue}")
        

     