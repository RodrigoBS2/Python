'''
Programa feito aqui

n = int(input())
j=1
w = n 
if w == 1:
    w = -1
for i in range(1,n+1):
    z = j
    while w >= 0 :
        print("  ",end='')
        w = w - 1
    while z > 0 :
        print("*",end='')
        z = z - 1
    j = j + 2
    w = n - i
    print()

w = 1
j = j - 4
for i in range (n+1,1,-1):
    z = j
    while w > 0 :
        print("  ",end='')
        w = w - 1
    while z > 0 :
        print("*",end='')
        z = z - 1
    j = j - 2
    w = n - i + 2 
    print()

    
print('\n\n')
'''










'''
Programa feito no site LoP



n = int(input())
j=1
w = n 
if w == 1:
    w = -1
for i in range(1,n+1):
    z = j
    while w >= 0 :
        print(" ",end='')
        w = w - 1
    while z > 0 :
        print("*",end='')
        z = z - 1
    j = j + 2
    w = n - i
    print()

w = 1
j = j - 4
for i in range (n+1,1,-1):
    z = j
    while w > 0 :
        print(" ",end='')
        w = w - 1
    while z > 0 :
        print("*",end='')
        z = z - 1
    j = j - 2
    w = n - i + 1 
    print()
'''




