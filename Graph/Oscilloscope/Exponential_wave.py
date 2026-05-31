import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Configuração da figura e dos eixos
fig, ax = plt.subplots()

# Título atualizado
plt.title("Simulação de Osciloscópio - Exponencial Decrescente")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")

# Parâmetros do sinal
periodo = 2.0         # Segundos (tempo que leva para a onda recomeçar)
V_max = 5.0           # Amplitude máxima (começo da exponencial)
constante_tempo = 0.5 # Constante Tau (tau): controla a velocidade do decaimento

frequencia_amostragem = 100 # pontos por segundo
tempo_visivel = 6.0         # Mostrar 3 períodos na tela (0 a 6s)

# Configuração fixa do eixo (Osciloscópio)
ax.set_xlim(0, tempo_visivel)
# Ajustei o limite Y para acomodar o pico de 5V e o zero
ax.set_ylim(-0.2, 5.5) 
ax.grid(True, linestyle='--', alpha=0.7)

# Eixo X fixo (os pontos da "tela")
x_vals = np.linspace(0, tempo_visivel, int(tempo_visivel * frequencia_amostragem))
# Cor verde "fósforo"
linha, = ax.plot(x_vals, np.zeros_like(x_vals), lw=2, color='lime') 

def calcular_onda_exponencial(t_array):
    """
    Calcula uma onda exponencial decrescente que se repete.
    A fórmula base é: V(t) = V_max * e^(-t/tau)
    """
    
    # 1. Sincronismo (O segredo do Trigger):
    # Usamos o módulo (%) para resetar o tempo para 0 dentro de cada período.
    # Isso garante que no início da tela (x=0), t_fase também seja 0.
    t_fase = t_array % periodo
    
    # 2. Aplicação da fórmula exponencial:
    # np.exp() calcula e^(x)
    valor_y = V_max * np.exp(-t_fase / constante_tempo)
    
    return valor_y

def atualizar(frame):
    # Adicionamos um ruído mínimo apenas para mostrar que o gráfico está "vivo"
    ruido = np.random.normal(0, 0.01, size=x_vals.shape)
    
    # Calculamos o sinal exponencial para todos os pontos da tela
    y_vals = calcular_onda_exponencial(x_vals) + ruido
    
    linha.set_ydata(y_vals)
    return linha,

# Animação simulando o refresh da tela
ani = animation.FuncAnimation(fig, atualizar, interval=50, blit=True, cache_frame_data=False)

plt.show()