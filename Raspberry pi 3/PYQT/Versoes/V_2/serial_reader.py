import time
import threading
import serial
import config

def iniciar_leitura_serial():
    try:
        ser = serial.Serial(config.PORTA_SERIAL, config.BAUD_RATE, timeout=0)
        ser.reset_input_buffer() 
    except Exception as e:
        print(f"Erro ao abrir a porta serial {config.PORTA_SERIAL}: {e}")
        return None

    def ler_serial_continuamente():
        buffer_serial = bytearray()
        while config.rodando:
            try:
                if ser.in_waiting:
                    buffer_serial.extend(ser.read(ser.in_waiting))
                    novas_tensoes = []
                    
                    i = 0
                    tamanho = len(buffer_serial)
                    
                    while i < tamanho - 1:
                        b1 = buffer_serial[i]
                        
                        if b1 >= 128:
                            b2 = buffer_serial[i+1]
                            if b2 < 128:
                                valor_adc = ((b1 & 0x7F) << 7) | b2
                                novas_tensoes.append((valor_adc / 4095.0) * 3.3)
                                i += 2
                            else:
                                i += 1
                        else:
                            i += 1
                            
                    del buffer_serial[:i]
                    
                    if novas_tensoes:
                        with config.buffer_lock:
                            config.buffer_interno.extend(novas_tensoes)
                else:
                    time.sleep(0.001)
            except Exception:
                pass

    thread_serial = threading.Thread(target=ler_serial_continuamente, daemon=True)
    thread_serial.start()
    return ser
    