from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import serial
import threading

# Configuração da porta serial (ajuste conforme necessário)
arduino = serial.Serial('COM12', 9600)  # Use a porta correta

# IP autorizado (o IP da máquina cliente permitida)
IP_AUTORIZADO = '127.0.0.1'  # Substitua pelo IP da máquina específica

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Variável global para armazenar o byte recebido
received_byte = None

@app.before_request
def limitar_acesso():
    # Obtém o IP do cliente que fez a requisição
    ip_cliente = request.remote_addr
    if ip_cliente != IP_AUTORIZADO:
        print(f"Acesso negado para o IP: {ip_cliente}")
        abort(403)  # Retorna erro 403 (Proibido)

def read_from_arduino():
    global received_byte
    while True:
        if arduino.in_waiting > 0:
            received_byte = arduino.read(1)  # Lê um byte do Arduino
            print(f"Byte recebido do Arduino: {received_byte}")

# Rota para receber o byte enviado pela interface
@app.route('/byte', methods=['POST'])
def receive_byte():
    data = request.get_json()
    byte_value = data.get('byte')
    print(f"Byte recebido: {byte_value}")

    # Envia o byte via serial
    arduino.write(byte_value.to_bytes(1, 'big'))
    print(f"Byte {byte_value} enviado para o ATmega328P.")

    return jsonify({'message': 'Byte recebido e enviado!', 'byte': byte_value}), 200

# Rota para enviar feedback do byte recebido do Arduino
@app.route('/feedback', methods=['GET'])
def send_feedback():
    if received_byte is not None:
        return jsonify({'byte': received_byte.hex()}), 200
    else:
        return jsonify({'byte': None}), 200

if __name__ == '__main__':
    # Inicia a thread para leitura do Arduino
    threading.Thread(target=read_from_arduino, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
