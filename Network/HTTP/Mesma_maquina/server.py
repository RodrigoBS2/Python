from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

@app.route('/byte', methods=['POST'])
def receive_byte():
    data = request.get_json()
    byte_value = data.get('byte')
    print(f"Byte recebido: {byte_value}")
    return jsonify({'message': 'Byte recebido com sucesso!', 'byte': byte_value}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
