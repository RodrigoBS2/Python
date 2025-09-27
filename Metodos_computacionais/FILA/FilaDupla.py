class DQueue:
    def __init__(self):
        self.queue = []
    
    def enqueueBack(self, e):
        self.queue.append(e)   

    def enqueueFront(self,e):
        self.queue.insert(0,e)          # O comando insert(i,x) é usado para inserir um elemnto "x" na posição "i" de uma fila
    
    def dequeueFront(self):
        if len(self.queue) !=0:
            self.queue.pop(0)
        else:
            print('Lista vazia')
    
    def dequeueBack(self):
        if len(self.queue) !=0:
            self.queue.pop()
        else:
            print('Lista vazia')
    
    def front(self):
        return self.queue[0]
    
    def back(self):
        return self.queue[-1]
    
    def show(self):
        print(self.queue)
    

