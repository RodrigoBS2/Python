# Tudo na mesma máquina

from flask import Flask, request, jsonify
from flask_cors import CORS
import serial

# Configuração da comunicação serial (ajuste a porta conforme necessário)
arduino = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela porta correta

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

@app.route('/byte', methods=['POST'])
def receive_byte():
    data = request.get_json()
    byte_value = data.get('byte')
    print(f"Byte recebido: {byte_value}")

    # Envia o byte para o ATmega328P via serial
    arduino.write(byte_value.to_bytes(1, 'big'))
    print(f"Byte {byte_value} enviado para o ATmega328P.")

    # Retorna uma resposta de sucesso
    return jsonify({'message': 'Byte recebido e enviado para o ATmega328P!', 'byte': byte_value}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
