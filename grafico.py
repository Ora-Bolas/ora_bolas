import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animacao_grafico():
    # Carregar os dados da posição do robô do arquivo pos_robo.txt
    with open("pos_robo.txt", "r") as file:
        robot_data = file.readlines()
        
    # Extrair as coordenadas x e y do robô
    robot_x = []
    robot_y = []
    for line in robot_data:
        _, x, y = map(float, line.strip().split())
        robot_x.append(x)
        robot_y.append(y)

    # Carregar os dados da posição da bola do arquivo dados.txt
    with open("dados.txt", "r") as file:
        ball_data = file.readlines()

    # Extrair as coordenadas x e y da bola
    ball_x = []
    ball_y = []
    for line in ball_data:
        _, x, y = map(float, line.strip().split())
        ball_x.append(x)
        ball_y.append(y)

    # Calcular a distância entre a bola e o robô
    def distance(x1, y1, x2, y2):
        return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Definir o número total de frames com base na duração total da animação (6 segundos a 100 fps)
    total_frames = 600

    # Função de animação
    def animate(frame):
        # Calcular o índice correspondente nas listas de dados
        ball_idx = int(frame * len(ball_x) / total_frames)
        robot_idx = int(frame * len(robot_x) / total_frames)
        
        plt.cla()
        plt.plot(robot_x[:robot_idx], robot_y[:robot_idx], 'b', label='Trajetória do Robô')
        plt.plot(ball_x[:ball_idx], ball_y[:ball_idx], 'r', label='Trajetória da Bola')
        plt.plot(ball_x[ball_idx], ball_y[ball_idx], 'ro', label='Posição Atual da Bola')
        plt.xlabel('Posição X')
        plt.ylabel('Posição Y')
        plt.title('Trajetória da Bola e do Robô')
        plt.grid(True)
        plt.legend()
        
        # Verificar a distância entre a bola e o robô
        d = distance(ball_x[ball_idx], ball_y[ball_idx], robot_x[robot_idx], robot_y[robot_idx])
        if d <= 0.115:  # Se a distância for menor ou igual a 0.115, o robô interceptou a bola
            plt.text(0.115, 0.115, 'Interceptação!', fontsize=15, ha='center')

    # Configurar a animação
    ani = FuncAnimation(plt.gcf(), animate, frames=total_frames, interval=20, repeat=False)

    plt.show()
