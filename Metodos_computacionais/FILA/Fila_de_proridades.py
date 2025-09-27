class Toy:
    def __init__(self,name,priority):
        self.name = name
        self.priority = priority    
    
    def getName(self):
        return self.name
    
    def getPriority(self):
        return self.priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self,n,p):
        t = Toy(n,p)
        if len(self.queue) == 0:
            self.queue.append(t)
        else:
            for i in range(len(self.queue)):
                if t.getPriority() > self.queue[i].getPriority():
                    self.queue.insert(i,t)
                    break
                if t.getPriority() < self.queue[-1].getPriority():
                    self.queue.append(t)

    def dequeue(self):
        if len(self.queue) != 0 :
            self.queue.pop(0)

    def front(self):
        return self.queue[0]


        