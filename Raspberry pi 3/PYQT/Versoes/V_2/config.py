import threading
from collections import deque

PORTA_SERIAL = '/dev/ttyUSB0' 
BAUD_RATE = 115200

FREQUENCIA_AMOSTRAGEM = 5700 
TEMPO_MAXIMO = 1.0 
TAMANHO_BUFFER = int(TEMPO_MAXIMO * FREQUENCIA_AMOSTRAGEM) * 2

# Objetos globais compartilhados para sincronização entre arquivos
buffer_lock = threading.Lock()
buffer_interno = deque([0.0] * TAMANHO_BUFFER, maxlen=TAMANHO_BUFFER)
rodando = True


