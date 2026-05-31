import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
from collections import deque
import numpy as np

# --- Configurações ---
PORTA_SERIAL = '/dev/ttyUSB0' 
BAUD_RATE = 115200

# Parâmetros do Osciloscópio
tempo_visivel = 0.5 
frequencia_amostragem = 2500 
max_pontos = int(tempo_visivel * frequencia_amostragem)
tensao_escala = 3.5 
posicao_y_inicial = 0.0 

# --- Configurações Iniciais do Trigger ---
trigger_ativado = False # Inicia desligado
nivel_trigger_atual = 2.0  
PONTOS_PRE_TRIGGER = int(max_pontos * 0.1) 
PONTOS_POS_TRIGGER = max_pontos - PONTOS_PRE_TRIGGER

# Buffer circular gigante para guardar o histórico 
TEMPO_MAXIMO_TELA = 2.0
tamanho_buffer_interno = int(TEMPO_MAXIMO_TELA * frequencia_amostragem) * 3
buffer_interno = deque([0.0] * tamanho_buffer_interno, maxlen=tamanho_buffer_interno)

# Buffers de exibição
y_data_tela = np.zeros(max_pontos)
x_data = np.linspace(0, tempo_visivel, max_pontos)

# --- Inicialização da Serial ---
try:
    ser = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=0.01)
except Exception as e:
    print(f"Erro ao abrir a porta serial: {e}")
    exit()

# --- Configuração da Figura e Eixos ---
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.40) 

plt.xlabel("Tempo (s) - Estimado")
plt.ylabel("Tensão (V)")

ax.set_xlim(0, tempo_visivel)
ax.set_ylim(-0.2 + posicao_y_inicial, tensao_escala + posicao_y_inicial)
ax.grid(True, linestyle='--', alpha=0.7)

# Desenha as linhas guia do Trigger (iniciam invisíveis)
linha_trigger_h = ax.axhline(nivel_trigger_atual, color='red', linestyle=':', alpha=0.5) 
linha_trigger_v = ax.axvline(x_data[PONTOS_PRE_TRIGGER], color='red', linestyle=':', alpha=0.5)
linha_trigger_h.set_visible(False)
linha_trigger_v.set_visible(False)

# Linha do gráfico
linha, = ax.plot(x_data, y_data_tela, lw=2, color='lime')

# Texto na tela
texto_info = ax.text(0.02, 0.95, '', transform=ax.transAxes, 
                     fontsize=12, verticalalignment='top', 
                     bbox=dict(boxstyle='round', facecolor='black', alpha=0.8, edgecolor='lime'),
                     color='lime')

# Estilização Escura
fig.patch.set_facecolor('#1e1e1e')
ax.set_facecolor('#000000')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(colors='white')
plt.title("Leitura do Fotodiodo", color='white')

# --- Configuração dos Sliders e Botão ---

ax_slider_tempo = plt.axes([0.15, 0.30, 0.7, 0.03], facecolor='black')
slider_tempo = Slider(ax=ax_slider_tempo, label='Tempo/Div (s)', valmin=0.1, valmax=TEMPO_MAXIMO_TELA, valinit=tempo_visivel, valstep=0.1, color='lime')
slider_tempo.label.set_color('white')
slider_tempo.valtext.set_color('white')

ax_slider_tensao = plt.axes([0.15, 0.22, 0.7, 0.03], facecolor='black')
slider_tensao = Slider(ax=ax_slider_tensao, label='Tensão Máx (V)', valmin=0.5, valmax=5.0, valinit=tensao_escala, valstep=0.1, color='cyan')
slider_tensao.label.set_color('white')
slider_tensao.valtext.set_color('white')

ax_slider_posicao = plt.axes([0.15, 0.14, 0.7, 0.03], facecolor='black')
slider_posicao_y = Slider(ax=ax_slider_posicao, label='Posição Y (V)', valmin=-4.0, valmax=4.0, valinit=posicao_y_inicial, valstep=0.1, color='magenta')
slider_posicao_y.label.set_color('white')
slider_posicao_y.valtext.set_color('white')

# Slider do Trigger (encurtado para caber o botão ao lado)
ax_slider_trigger = plt.axes([0.15, 0.06, 0.55, 0.03], facecolor='black')
slider_trigger = Slider(ax=ax_slider_trigger, label='Trigger (V)', valmin=0.1, valmax=4.0, valinit=nivel_trigger_atual, valstep=0.1, color='yellow')
slider_trigger.label.set_color('white')
slider_trigger.valtext.set_color('white')

# Botão de Ativar/Desativar Trigger
ax_botao_trigger = plt.axes([0.75, 0.06, 0.1, 0.03])
botao_trigger = Button(ax_botao_trigger, 'Trigger: OFF', color='darkred', hovercolor='red')
botao_trigger.label.set_color('white')


# --- Funções de Atualização dos Controles ---
def atualizar_escala_tempo(val):
    global tempo_visivel, max_pontos, PONTOS_PRE_TRIGGER, PONTOS_POS_TRIGGER
    global x_data, y_data_tela
    
    tempo_visivel = slider_tempo.val
    max_pontos = int(tempo_visivel * frequencia_amostragem)
    PONTOS_PRE_TRIGGER = int(max_pontos * 0.1)
    PONTOS_POS_TRIGGER = max_pontos - PONTOS_PRE_TRIGGER
    
    x_data = np.linspace(0, tempo_visivel, max_pontos)
    y_data_tela = np.zeros(max_pontos)
    
    ax.set_xlim(0, tempo_visivel)
    linha.set_xdata(x_data)
    linha_trigger_v.set_xdata([x_data[PONTOS_PRE_TRIGGER], x_data[PONTOS_PRE_TRIGGER]])
    fig.canvas.draw_idle()

def atualizar_eixo_y(val):
    escala = slider_tensao.val
    offset = slider_posicao_y.val
    ax.set_ylim(-0.2 + offset, escala + offset)
    fig.canvas.draw_idle()

def atualizar_trigger(val):
    global nivel_trigger_atual
    nivel_trigger_atual = slider_trigger.val
    linha_trigger_h.set_ydata([nivel_trigger_atual, nivel_trigger_atual])
    fig.canvas.draw_idle()

def alternar_trigger(event):
    global trigger_ativado
    trigger_ativado = not trigger_ativado
    
    if trigger_ativado:
        botao_trigger.label.set_text('Trigger: ON')
        botao_trigger.color = 'darkgreen'
        botao_trigger.hovercolor = 'green'
        linha_trigger_h.set_visible(True)
        linha_trigger_v.set_visible(True)
    else:
        botao_trigger.label.set_text('Trigger: OFF')
        botao_trigger.color = 'darkred'
        botao_trigger.hovercolor = 'red'
        linha_trigger_h.set_visible(False)
        linha_trigger_v.set_visible(False)
        
    fig.canvas.draw_idle()

slider_tempo.on_changed(atualizar_escala_tempo)
slider_tensao.on_changed(atualizar_eixo_y)
slider_posicao_y.on_changed(atualizar_eixo_y)
slider_trigger.on_changed(atualizar_trigger)
botao_trigger.on_clicked(alternar_trigger)

# --- Função de Animação Principal ---
def atualizar(frame):
    novos_dados = False
    
    while ser.in_waiting:
        try:
            linha_serial = ser.readline().decode('utf-8').strip()
            if linha_serial:
                valor_adc = int(linha_serial)
                tensao = (valor_adc / 4095.0) * 3.3
                
                buffer_interno.append(tensao)
                novos_dados = True
                
        except ValueError:
            pass
        except Exception:
            pass
            
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
            # Modo Livre (Sem Trigger)
            novo_y = arr[-max_pontos:]
            atualizar_grafico = True

        if atualizar_grafico and len(novo_y) == len(y_data_tela):
            y_data_tela[:] = novo_y
        
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
    
    return linha, texto_info

ani = animation.FuncAnimation(fig, atualizar, interval=15, blit=True, cache_frame_data=False)

def ao_fechar(event):
    ser.close()
    print("Porta serial fechada.")

fig.canvas.mpl_connect('close_event', ao_fechar)
plt.show()