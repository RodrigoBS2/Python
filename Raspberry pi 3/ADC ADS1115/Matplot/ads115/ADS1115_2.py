import time
import threading
import queue
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
from collections import deque
import numpy as np

# --- Bibliotecas do Hardware (Raspberry Pi + ADS1115) ---
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1x15 as ads1x15

# --- Configuração do I2C e ADS1115 ---
try:
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c, data_rate=860) 
    chan = AnalogIn(ads, ads1x15.Pin.A0) 
except Exception as e:
    print(f"Erro ao inicializar o ADS1115: {e}")
    exit()

# --- Parâmetros do Osciloscópio ---
tempo_visivel = 0.5 
frequencia_amostragem = 860 
max_pontos = int(tempo_visivel * frequencia_amostragem)
tensao_escala = 4.0 
posicao_y_inicial = 0.0 

# --- Configurações Iniciais do Trigger ---
trigger_ativado = False
nivel_trigger_atual = 2.0  
PONTOS_PRE_TRIGGER = int(max_pontos * 0.1) 
PONTOS_POS_TRIGGER = max_pontos - PONTOS_PRE_TRIGGER

# Buffer circular
TEMPO_MAXIMO_TELA = 2.0
tamanho_buffer_interno = int(TEMPO_MAXIMO_TELA * frequencia_amostragem) * 3
buffer_interno = deque([0.0] * tamanho_buffer_interno, maxlen=tamanho_buffer_interno)

# Fila e controle
fila_dados = queue.Queue()
rodando = True
precisa_redesenhar_fundo = False # FLAG NOVA PARA CORRIGIR O GHOSTING

# Buffers de exibição
y_data_tela = np.zeros(max_pontos)
x_data = np.linspace(0, tempo_visivel, max_pontos)

# --- Thread de Leitura do ADC ---
def ler_adc_continuamente():
    periodo_alvo = 1.0 / 860.0 
    while rodando:
        inicio = time.perf_counter()
        try:
            fila_dados.put(chan.voltage)
        except Exception:
            pass
        tempo_gasto = time.perf_counter() - inicio
        if tempo_gasto < periodo_alvo:
            time.sleep(periodo_alvo - tempo_gasto)

thread_adc = threading.Thread(target=ler_adc_continuamente, daemon=True)
thread_adc.start()

# --- Configuração da Figura e Eixos ---
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.40) 

plt.xlabel("Tempo (s) - Estimado")
plt.ylabel("Tensão (V)")

ax.set_xlim(0, tempo_visivel)
ax.set_ylim(-0.2 + posicao_y_inicial, tensao_escala + posicao_y_inicial)
ax.grid(True, linestyle='--', alpha=0.7)

linha_trigger_h = ax.axhline(nivel_trigger_atual, color='red', linestyle=':', alpha=0.5) 
linha_trigger_v = ax.axvline(x_data[PONTOS_PRE_TRIGGER], color='red', linestyle=':', alpha=0.5)
linha_trigger_h.set_visible(False)
linha_trigger_v.set_visible(False)

linha, = ax.plot(x_data, y_data_tela, lw=2, color='lime')

texto_info = ax.text(0.02, 0.95, '', transform=ax.transAxes, 
                     fontsize=12, verticalalignment='top', 
                     bbox=dict(boxstyle='round', facecolor='black', alpha=0.8, edgecolor='lime'),
                     color='lime')

fig.patch.set_facecolor('#1e1e1e')
ax.set_facecolor('#000000')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(colors='white')
plt.title("Leitura do Fotodiodo (ADS1115 via I2C)", color='white')

# --- Configuração dos Sliders e Botão ---
ax_slider_tempo = plt.axes([0.15, 0.30, 0.7, 0.03], facecolor='black')
slider_tempo = Slider(ax=ax_slider_tempo, label='Tempo/Div', valmin=0.1, valmax=TEMPO_MAXIMO_TELA, valinit=tempo_visivel, valstep=0.1, color='lime')
slider_tempo.label.set_color('white')
slider_tempo.valtext.set_color('white')

ax_slider_tensao = plt.axes([0.15, 0.22, 0.7, 0.03], facecolor='black')
slider_tensao = Slider(ax=ax_slider_tensao, label='Tensão Máx', valmin=0.5, valmax=5.0, valinit=tensao_escala, valstep=0.1, color='cyan')
slider_tensao.label.set_color('white')
slider_tensao.valtext.set_color('white')

ax_slider_posicao = plt.axes([0.15, 0.14, 0.7, 0.03], facecolor='black')
slider_posicao_y = Slider(ax=ax_slider_posicao, label='Posição Y', valmin=-4.0, valmax=4.0, valinit=posicao_y_inicial, valstep=0.1, color='magenta')
slider_posicao_y.label.set_color('white')
slider_posicao_y.valtext.set_color('white')

ax_slider_trigger = plt.axes([0.15, 0.06, 0.55, 0.03], facecolor='black')
slider_trigger = Slider(ax=ax_slider_trigger, label='Trigger (V)', valmin=0.1, valmax=4.0, valinit=nivel_trigger_atual, valstep=0.1, color='yellow')
slider_trigger.label.set_color('white')
slider_trigger.valtext.set_color('white')

ax_botao_trigger = plt.axes([0.75, 0.06, 0.1, 0.03])
botao_trigger = Button(ax_botao_trigger, 'Trig: OFF', color='darkred', hovercolor='red')
botao_trigger.label.set_color('white')

# --- Funções de Atualização dos Controles ---
def atualizar_escala_tempo(val):
    global tempo_visivel, max_pontos, PONTOS_PRE_TRIGGER, PONTOS_POS_TRIGGER
    global x_data, y_data_tela, precisa_redesenhar_fundo
    
    tempo_visivel = slider_tempo.val
    max_pontos = int(tempo_visivel * frequencia_amostragem)
    PONTOS_PRE_TRIGGER = int(max_pontos * 0.1)
    PONTOS_POS_TRIGGER = max_pontos - PONTOS_PRE_TRIGGER
    
    x_data = np.linspace(0, tempo_visivel, max_pontos)
    y_data_tela = np.zeros(max_pontos)
    
    ax.set_xlim(0, tempo_visivel)
    linha.set_xdata(x_data)
    linha_trigger_v.set_xdata([x_data[PONTOS_PRE_TRIGGER], x_data[PONTOS_PRE_TRIGGER]])
    precisa_redesenhar_fundo = True # Sinaliza para limpar o ghosting

def atualizar_eixo_y(val):
    global precisa_redesenhar_fundo
    escala = slider_tensao.val
    offset = slider_posicao_y.val
    ax.set_ylim(-0.2 + offset, escala + offset)
    precisa_redesenhar_fundo = True # Sinaliza para limpar o ghosting

def atualizar_trigger(val):
    global nivel_trigger_atual, precisa_redesenhar_fundo
    nivel_trigger_atual = slider_trigger.val
    linha_trigger_h.set_ydata([nivel_trigger_atual, nivel_trigger_atual])
    precisa_redesenhar_fundo = True

def alternar_trigger(event):
    global trigger_ativado, precisa_redesenhar_fundo
    trigger_ativado = not trigger_ativado
    
    if trigger_ativado:
        botao_trigger.label.set_text('Trig: ON')
        botao_trigger.color = 'darkgreen'
        linha_trigger_h.set_visible(True)
        linha_trigger_v.set_visible(True)
    else:
        botao_trigger.label.set_text('Trig: OFF')
        botao_trigger.color = 'darkred'
        linha_trigger_h.set_visible(False)
        linha_trigger_v.set_visible(False)
        
    precisa_redesenhar_fundo = True

slider_tempo.on_changed(atualizar_escala_tempo)
slider_tensao.on_changed(atualizar_eixo_y)
slider_posicao_y.on_changed(atualizar_eixo_y)
slider_trigger.on_changed(atualizar_trigger)
botao_trigger.on_clicked(alternar_trigger)

# --- Função de Animação Principal ---
def atualizar(frame):
    global precisa_redesenhar_fundo
    novos_dados = False
    
    # Se algum slider foi movido, força um redesenho limpo antes do blit
    if precisa_redesenhar_fundo:
        fig.canvas.draw()
        precisa_redesenhar_fundo = False

    # Esvazia a fila de forma otimizada para a CPU da Raspberry Pi
    q_size = fila_dados.qsize()
    for _ in range(q_size):
        try:
            buffer_interno.append(fila_dados.get_nowait())
            novos_dados = True
        except queue.Empty:
            break
            
    if novos_dados and len(buffer_interno) > max_pontos:
        arr = np.array(buffer_interno)
        atualizar_grafico = False
        
        if trigger_ativado:
            condicao_subida = (arr[:-1] < nivel_trigger_atual) & (arr[1:] >= nivel_trigger_atual)
            indices_trigger = np.where(condicao_subida)[0]
            
            triggers_validos = [i for i in indices_trigger if (i >= PONTOS_PRE_TRIGGER) and ((len(arr) - i - 1) >= PONTOS_POS_TRIGGER)]
            
            if triggers_validos:
                idx_trigger = triggers_validos[-1] + 1 
                novo_y = arr[idx_trigger - PONTOS_PRE_TRIGGER : idx_trigger + PONTOS_POS_TRIGGER]
                atualizar_grafico = True
        else:
            novo_y = arr[-max_pontos:]
            atualizar_grafico = True

        if atualizar_grafico and len(novo_y) == len(y_data_tela):
            y_data_tela[:] = novo_y
            
            # Cálculo de RMS e Frequência mantidos
            tensao_rms = np.sqrt(np.mean(np.square(y_data_tela)))
            frequencia_hz = 0.0
            acima_limiar = y_data_tela > 2.0 
            mudancas = np.diff(acima_limiar.astype(int))
            bordas_subida = np.where(mudancas == 1)[0]
            
            if len(bordas_subida) > 1:
                periodos_em_pontos = np.diff(bordas_subida)
                periodo_medio = np.mean(periodos_em_pontos)
                frequencia_hz = frequencia_amostragem / periodo_medio

            texto_legenda = (f'Tensão RMS: {tensao_rms:.3f} V\n'
                             f'Frequência: {frequencia_hz:.1f} Hz')
                             
            linha.set_ydata(y_data_tela)
            texto_info.set_text(texto_legenda)
    
    return linha, texto_info, linha_trigger_h, linha_trigger_v

# OTIMIZAÇÃO: interval de 15 (66 fps) reduzido para 50 (20 fps) para aliviar a Pi 3
ani = animation.FuncAnimation(fig, atualizar, interval=50, blit=True, cache_frame_data=False)

def ao_fechar(event):
    global rodando
    rodando = False 
    print("Osciloscópio encerrado.")

fig.canvas.mpl_connect('close_event', ao_fechar)
plt.show()
