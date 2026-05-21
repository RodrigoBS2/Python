from tipos_caneca import *

print("Canecas personalizadas!\nAqui você pode tanto escolher uma caneca já personalizada ou criar uma nova!")
Fc = input("Digite 'E' se preferir optar por uma ja feita. Digite 'C' para criar uma.\n") 
while 1:
    if Fc == 'E':
        print('As canecas personalizadas disponiveis são:')
        Bat.mostrarDados()
        Hf.extra()
        break
    elif Fc == 'C':
        C.logo = input("Digite a logo da caneca: ")
        C.nome = input("Digite o nome da caneca: ")
        C.cor = input("digite a cor da caneca: ")
        C.mostrarDados()
        break
    else:
        print("ERRO! Digite novamente \n")
        Fc = input()
