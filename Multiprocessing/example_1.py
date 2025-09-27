# Importação de bibliotecas 
from multiprocessing import Process
import logging
import time

#Criação do arquivo Log
logging.basicConfig(filename="C:/Users/Rsilv/Desktop/programacao/Python/Multiprocessing/To_Ex_1/mesage.log",
                    filemode='w', encoding='utf-8',format='%(asctime)s  %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
 
time.sleep(1)   # Delay de um segundo 

# Função para enviar a string "mensagem" para o arquivo "mesage.log"
def Mesage():
        while 1:
            logging.debug("mensagem")  
            time.sleep(3)
            


if __name__ == "__main__":  # confirms that the code is under main function
    # Criando o processo
    p = Process(target = Mesage) # Processo da função Mesage
    p.start()   # Inicializa o processo Mesage
    while 1:
        command_send = input("Envie um comando: ")
        if command_send == 'S':
            break
    p.join()

