from tipos_caneca import *

print("Canecas personalizadas!\nAqui você pode tanto escolher uma caneca já personalizada ou criar uma nova!")
Fc = input("Digite 'E' se preferir optar por uma ja feita. Digite 'C' para criar uma.\n") 
if Fc == 'E':
    print('As canecas personalizadas disponiveis são:')
    Bat.extra()
    Hf.extra()
if Fc == 'C':
    print('')