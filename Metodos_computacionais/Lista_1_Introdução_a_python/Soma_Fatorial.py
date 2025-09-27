def fatorial (numero):
    m = 1
    if numero <= 1:
        return 1
    while numero > 1:
        m = m * numero
        numero-=1
    return m

def somaFat (numero1, numero2):
    return print(f'{numero1}! + {numero2}! = {fatorial(numero1) + fatorial(numero2)}')

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
somaFat (valor1, valor2)

