class Pilha:                                #Criando a classe pilha que irá armazenar os valores da base convertida
    def __init__(self):
        self.pilha = []
    
    def base(self,numero,base):                 # Método para obter o valor do numero convertido pela base requerida
        while numero > base:                    # O Ciclo while ficará dividindo o número pela base repetidas vezes até que o numero seja igual ou menor que o valor da base 
            self.pilha.append(numero%base)      # A pilha irá armazenar o resto da divisão do "numero" pela "base"
            numero = numero//base               # A variavel "numero" receberá a divisão numero / base para que este possa obter um novo valor para o resto (numero%base)
        self.pilha.append(numero)               # Após o ciclo o número será inserido no inicio da fila 
    
    def printar(self):                        # Metodo para printar o número convertido na tela
        while len(self.pilha) != 0:
            print(self.pilha.pop(),end='')

p = Pilha()
numero = int(input())                               # Inserir o número
base = int(input())                               # Inserir a base

p.base(numero,base)
p.printar()