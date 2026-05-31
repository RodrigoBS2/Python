import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Configuração da figura e dos eixos
fig, ax = plt.subplots()

plt.title("Simulação de Osciloscópio (Sinal Trigado)")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")

# Parâmetros do sinal
periodo = 2.0  # segundos
amplitude = 3.3
frequencia_amostragem = 100 # pontos por segundo
tempo_visivel = 4.0 # Mostrar 2 períodos na tela (0 a 4s)

# Configuração fixa do eixo (como a tela de um osciloscópio)
ax.set_xlim(0, tempo_visivel)
ax.set_ylim(-0.5, 4.0)
ax.grid(True, linestyle='--', alpha=0.7) # Adiciona grade para parecer osciloscópio

# Eixo X fixo (os pontos da "tela")
x_vals = np.linspace(0, tempo_visivel, int(tempo_visivel * frequencia_amostragem))
linha, = ax.plot(x_vals, np.zeros_like(x_vals), lw=2, color='lime') # Cor verde "fósforo"

def calcular_onda_quadrada(t_array):
    """
    Calcula a onda quadrada. 
    Como queremos 'trigado', o t=0 sempre inicia em nível alto (subida).
    """
    # (t % periodo) < (periodo / 2) cria o pulso começando no 0
    return np.where((t_array % periodo) < (periodo / 2), amplitude, 0.0)

def atualizar(frame):
    # Em um osciloscópio real, o sinal tem pequenos ruídos ou variações
    # Adicionamos um ruído mínimo apenas para mostrar que o gráfico está "vivo"
    ruido = np.random.normal(0, 0.02, size=x_vals.shape)
    
    # Calculamos o sinal para todos os pontos da tela de uma vez
    y_vals = calcular_onda_quadrada(x_vals) + ruido
    
    linha.set_ydata(y_vals)
    return linha,

# Animação simulando o refresh da tela (60 FPS aprox. com interval=16)
ani = animation.FuncAnimation(fig, atualizar, interval=50, blit=True, cache_frame_data=False)

plt.show()