import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import collections
import time


# Configuração da figura e dos eixos
fig, ax = plt.subplots()    # Retorna um tupla com dois objetos como elementos da tupla (Figure e Axes)

plt.title("Leitura analógica")
plt.xlabel("Tempo decorrido (segundos)")
plt.ylabel("Tensão (V)")

ax.set_ylim(0.0, 5.0)

# Deques para armazenar os dados do eixo X (tempo) e Y (valores)
x_data = collections.deque(maxlen=200)
y_data = collections.deque(maxlen=200)

linha, = ax.plot([], [], lw=1, color='blue')     # Retorna uma lista com objetos do tipo Line2D como elementos da lista. Neste caso retornou uma lista com apenas um elemento do tipo Line2D

# Registra o tempo em que o programa iniciou
tempo_inicial = time.time()

# Janela de visualização do gráfico (ex: mostrar apenas os últimos 10 segundos)
janela_de_tempo = 10 

#Remover a visualização do eixo x no gráfico
ax.set_xticks([])

def atualizar(frame):
    # Calcula quantos segundos se passaram desde o início do programa
    tempo_atual = time.time() - tempo_inicial
    
    # Tensão
    tensao = round(random.uniform(0.0, 3.3),2) # Gerando número do tipo float entre 0.0 a 3.3 usando random e estabelecendo duas casas decimais usando o round
    
    x_data.append(tempo_atual)
    y_data.append(tensao)
    
    linha.set_data(x_data, y_data)
    
    # Atualiza o eixo X para acompanhar o tempo decorrido
    if tempo_atual > janela_de_tempo:
        # Move o gráfico mantendo sempre 'janela_de_tempo' segundos visíveis
        ax.set_xlim(tempo_atual - janela_de_tempo, tempo_atual)
    else:
        # Nos primeiros 10 segundos, o eixo X fica fixo de 0 a 10
        ax.set_xlim(0, janela_de_tempo)
        
    return linha,

# Animação rodando a cada 100 milissegundos
ani = animation.FuncAnimation(fig, atualizar, interval=50, cache_frame_data=False)

plt.show()