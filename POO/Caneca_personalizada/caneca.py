class Caneca:
    def __init__(self,logo,nome,cor):
      self.logo = logo
      self.nome = nome
      self.cor = cor
      self.status = 'Cheio'
      
    
    def beber(self):
      self.status= 'Vazio'
      print('Bebendo a caneca ', self.nome)
      print('Status da caneca : ',self.status)

    def encher(self):
      self.status = 'Cheio'
      print('Enchendo a caneca ', self.nome)
      print('Status da caneca : ', self.status)

    def alterar_caneca(self):
      self.nome = input('Digite um novo nome: ')
      self.logo = input('Digite um novo logo: ')
      self.cor = input('Digite uma nova cor: ')
      print('\n\n\n')
      self.mostrarDados()

    def mostrarDados(self):
      print(f'Caneca: \n  Logo: {self.logo}\n  Nome: {self.nome}\n  Cor: {self.cor}\n')
    
class Caneca_Homem_de_ferro(Caneca):
  def __init__(self):
    super().__init__('Marvel','Homem de ferro', 'Amarela e vermelho')         # Usando "super().Nome_da_função(parametros_dessa_função)" vc não precisa digitar novamente os codigos da função ja escrita
  def extra(self):
    self.mostrarDados()
    print("Soy el hombre de hierro!")

class Caneca_Batman(Caneca):
  def __init__(self):
    super().__init__('DC','Batman', 'Preto')
  def extra(self):
    self.mostrarDados()
    print('Soy Batman!')
