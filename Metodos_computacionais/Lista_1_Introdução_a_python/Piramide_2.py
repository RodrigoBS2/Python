n = int(input())
j=1
w = n 
for i in range(1,n+1):                  # Cronstrução da piramide q vai de 1 a n
    z = j                               
    while w > 1 :                       # while w ---> quantidade de espaçamento q sera printado
        print("  ",end='')
        w = w - 1
    while z > 0 :                       # while z ---> quantidade de vezes q o numero sera imprimido pela variavel i. Ela reperesenta os numeros da piramide
        print(i,end='')
        z = z - 1
    j = j + 2
    w = n - i
    print()                             # pula para a proxima linha e fazendo o ciclo for novamente só q agora o numero imprimido foi acrescentado de um (caso i > 1) de um

w = 1
j = j - 4                               # Apos ciclo for da piramede o valor de j é j + 2 é necessário diminuir esse valor para o começo da piramide invertida. logo j = j - 4 

for i in range (n-1,0,-1):              # Cronstrunçao da piramide invertida q vai de n-1 a 1
    z = j
    while w > 0 :                       # while w ---> quantidade de espaçamento q sera printado
        print("  ",end='')
        w = w - 1
    while z > 0 :                       # while z ---> quantidade de vezes q o numero sera imprimido pela variavel i 
        print(i,end='')
        z = z - 1
    j = j - 2
    w = n - i + 1
    print()                             # pula para a proxima linha e fazendo o ciclo for novamente só q agora o numero imprimido i foi subtraido de um
