class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,e):
        self.queue.append(e)
    def dequeue(self):
        if len(self.queue) == 0:
            print('Fila vazia')
        else:
            self.queue.pop(0)
    def front(self):
        return self.queue[0]
    def show(self):
        print(self.queue)
     