class Pilha:
                                            # Para esse código pimeiramente foi tirado todas os espaços, depois tiradas todas as letras e por último foi feito uma comparação dos elementos atraves da eliminação destes caso os mesmos forem um o inverso do outro. Sendo confirmado a comparação, os elementos comparados serão eliminados e uma nova analise sera feita com o tamanho menor da pilha. Fazendo esse procedimento até que não sobre nehnhum elemento (sendo assim considerado como bem formado), caso contrário, se um elemento não for o inverso do seguinte, pode-se considerar como mal formado. Serão encontrados inicialmente aqueles que sejam do formato ']','}' ou ')' e depois verificar se o elemento anterior a esse é da fomra '[', '{' ou '('.
    def __init__(self):
        self.pilha = []
   
    def inserir(self,Input):
        while len(Input) != 0:
            self.pilha.append(Input.pop())

    def eliminiar_letras(self): #---------------> Método para eliminar todas as letras da pilha
        aux = []    #---------------------------> Lista auxiliar
        L=['[','{','(',']','}',')']#------------> Lista "L" para comparar se os elemntos da "self.pilha" são iguais a algum desses elementos
        while len(self.pilha) != 0:
            z = self.pilha.pop()                # removendo cada elemento da self.pilha e comparando com elementos da lista "L"
            for i in L:
                if z == i:
                    aux.append(z)
        self.pilha = aux

        
    def verificar(self):
        g = 0 #------> Usado para quebrar os ciclos 'for' quando uma comparação entre um elemnto e o seu anterior forem um o inverso do outro ( por exemplo '{'e '}')
        w = 0 #------> Usado para receber o valor da posição do elelmento. Se a comparação entre dois elementos consecutivos for verdadeira (um o inverso do outro), w será 0 novamente para uma nova contagem mas com o tamanho da fila reduzida (uma fila sem esses dois elementos que foram comparados)
        z = ''#------> Receberar o valor anterior de 'i'. Sera o elemento usado para comparar com 'i'
        L=['[','{','(',']','}',')']  #-----------> 'L' é uma lista com os parênteses, colchetes e chaves para auxiliar durante a comparação dos elementos da "self.pilha"
        
        while len(self.pilha) != 0:
            for i in self.pilha:
                for n in range(3,len(L)):#--------> Irá verificar se 'i' é igual aos três ultimos elementos da lista 'L' e em seguida ira comparar se o elemento anterior é o seu inverso
                    if i == L[n]:
                        if z == L[n-3]:#------> verificara se o elemento anterior é o seu inverso
                            self.pilha.pop(w-1)     # Caso for verdadeiro, será removido os dois elementos comparados e os dois ciclos 'for' serão quebrados para uma nova análise
                            self.pilha.pop(w-1)
                            g = 1
                            break           #---> Irá quebrar o segundo ciclo for ("for n in range...")
                        else:#-----> Caso a segunda comparação(if z ==L[n-3]) for falsa
                            return print('mal formado')
                w = w + 1   #------------------------------------> Caso as comparações forem falsa, sera adicionado mais uma posição em w e z receberar o antigo valor de i 
                z = i
                if g == 1:  
                    w = 0  #-----> será realizado uma nova analise de self.pilha mas com seu tamanho reduzido
                    break  #---> Irá quebrar o primeiro ciclo for ("for n in range...")
            g = 0
        return  print('bem formado')
        
      
P = Pilha()
Input = list(input())
P.inserir(Input)
P.eliminiar_letras()
P.verificar()