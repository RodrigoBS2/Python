from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import serial

# Configuração da porta serial (ajuste conforme necessário)
arduino = serial.Serial('COM3', 9600)  # Use a porta correta

# IP autorizado (o IP da máquina cliente permitida)
IP_AUTORIZADO = '192.168.1.100'  # Substitua pelo IP da máquina específica

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

@app.before_request
def limitar_acesso():
    # Obtém o IP do cliente que fez a requisição
    ip_cliente = request.remote_addr
    if ip_cliente != IP_AUTORIZADO:
        print(f"Acesso negado para o IP: {ip_cliente}")
        abort(403)  # Retorna erro 403 (Proibido)

@app.route('/byte', methods=['POST'])
def receive_byte():
    data = request.get_json()
    byte_value = data.get('byte')
    print(f"Byte recebido: {byte_value}")

    # Envia o byte via serial
    arduino.write(byte_value.to_bytes(1, 'big'))
    print(f"Byte {byte_value} enviado para o ATmega328P.")

    return jsonify({'message': 'Byte recebido e enviado!', 'byte': byte_value}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
