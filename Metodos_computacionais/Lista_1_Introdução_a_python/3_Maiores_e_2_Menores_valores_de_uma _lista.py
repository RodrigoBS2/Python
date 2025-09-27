
def ordem_crescente(lista):
    aux = []
    for i in range(len(lista)):     #   Adicionando os elementos na lista auxiliar
        aux.append(lista[i])

    for i in range(len(lista)-2):   # Fazendo dois ciclos for para trocar a ordem dos elementos n*(n-1) vezes. Aqueles de maior valor são trocados de lugar em direção ao topo da lista
        for j in range(len(lista)-1):
            x = aux[j]
            y = aux[j+1]
            if aux[j] > aux[j+1]:
                aux[j] = y
                aux[j+1] = x  
    return print(f'{aux[-1]} {aux[-2]} {aux[-3]} {aux[0]} {aux[1]}')
      


lista = [1,2,3,4,5]
ordem_crescente(lista)

    