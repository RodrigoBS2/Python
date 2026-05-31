numeros =[5,1,9,3]
tamanho = len(numeros)

for i in range(tamanho - 1):
    for j in range(tamanho - i - 1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

print("Lista ordenada:")
for i in range(tamanho):
    print(numeros[i], end=" ")
print('') 

