# Importação de bibliotecas Serial e Time
import serial
import time


# Habilitar uma porta para comunicação serial (nesse caso será via Bluetooth). O bluetooth do computador está conectado na porta COM4
ser = serial.Serial('COM5', 9600, timeout=1)  
time.sleep(2)   # Delay de dois segundos

while 1: # Loop infinito para mais de uma mensagem pela porta serial   
  Mensagem = input('Digite a mesnagem: ')  ##
  Mensagem = Mensagem + '\r'  ## Caractere adicional que indicada a finalização da mensagem q será enviada
  ser.write(Mensagem.encode())  ## Envio da mensagem para serial (COM5) aonde o bluetooth está conctado
  
  
  
 
  

    
