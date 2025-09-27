# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     # cria um novo socket s usando o IPv4 (AF_INET) e o protocolo TCP (SOCK_STREAM).
    s.bind((HOST, PORT))                                         # Este método associa o socket s a um endereço e porta específicos, que são representados por HOST e PORT.
    s.listen()                                                   # Este método coloca o socket em modo de escuta, permitindo que ele aceite conexões de clientes. O número de conexões em espera pode ser especificado, mas se não for, o padrão é geralmente suficiente.
    conn, addr = s.accept()                                      # O método accept() aguarda uma conexão de um cliente. Quando um cliente se conecta, ele retorna uma nova tupla:
                                                                    #   conn: Um novo socket que será usado para a comunicação com o cliente.
                                                                    #   addr: Um tupla contendo o endereço do cliente (IP e porta)                                                            
    with conn:                                                   # conn será fechado automaticamente quando sair do bloco.
        print(f"Connected by {addr}")                            
        while True:
            data = conn.recv(1024)                               # O método recv(1024) recebe até 1024 bytes de dados do socket conn. Se o cliente não enviar mais dados, esse método retornará uma string vazia.
            if not data:
                break
            print(f"Server received {data!r}")
            conn.sendall(data)                                   # O método sendall(data) envia todos os dados recebidos de volta para o cliente. O sendall() é usado em vez de send() para garantir que todos os dados sejam enviados, mesmo que isso exija múltiplas chamadas ao sistema.