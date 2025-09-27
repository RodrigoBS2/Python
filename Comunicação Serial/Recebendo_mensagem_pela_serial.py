# O programa irá receber mensagem de números que serão convertidos para float
# Importação de bibliotecas Serial e Time
import serial
import time

# Habilitar uma porta para comunicação serial (nesse caso será via Bluetooth). O bluetooth do computador está conectado na porta COM4
ser = serial.Serial("COM12", 9600, timeout = 1)  
time.sleep(1)   # Delay de dois segundos

# Declara lista que receberá os dados via serial
Lista = []

while 1: # Loop infinito para mais de uma mensagem pela porta serial   
  Mensagem = ser.readline().decode('ascii').strip() ## Lê o dado q está na porta serial e o converte para tabela ascii. 
                                                    ##  O "strip()" é usado para limpar caracteres adicionais como por exemplo o "\r\n" que geralmente fica no final de cada mensagem enviada. 
  
  if Mensagem != "O": # A string "O" será o ultimo dado a ser enviado. Enquanto isso qualquer dado diferente dele será inserido na lista "Lista"
    Lista.append(float(Mensagem))  # Converte o dado para float e o adiciona em"Lista"
  
  else: # Quando chegar no dado "O", será printado na tela os dados inseridos em "Lista". Depois "Lista" será limpado e um delay de 1s será adicionado.  
    print(Lista)
    Lista.clear()  
    time.sleep(1)  
    
