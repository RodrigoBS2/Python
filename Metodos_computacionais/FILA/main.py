# Para fila simples 

from Fila import Queue
Q = Queue()

Q.show()
Q.dequeue()

Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)

Q.show()
print(f"O primeiro elemento da fila é {Q.front()}")

Q.dequeue()
Q.dequeue()

Q.show()

 


# Para fila dupla 
'''
from FilaDupla import DQueue
D = DQueue()
D.show()
D.dequeueFront()
D.dequeueBack()
print('\n')
# Inserindo elementos na fila tanto no começo quanto no final
D.enqueueFront(1)   # No começo
D.enqueueBack(2)    # No final  
D.enqueueBack(3)    # No final
D.show()
print('\n')
# Inserindo elementos no começo da fila:
D.enqueueFront(0)
D.enqueueFront(-1)
# Inserindo elementos no final da fila:
D.enqueueBack(4)
D.enqueueBack(5)
D.show()
print('\n')
# Removendo um elemnto no começo e no final da fila:
D.dequeueFront()
D.dequeueFront()
D.dequeueBack()
D.dequeueBack()
D.show()
print('\n')
# Mostrando o primeiro elemento da fila e o ultimo
print(D.front())
print(D.back())

'''


'''
Existe uma biblioteca chamada collections deque que tem todas essas funções para fila dupla
'''