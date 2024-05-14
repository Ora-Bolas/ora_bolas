from math import sqrt, atan, cos, sin
import matplotlib.pyplot as plt


def distancia(xRobo, yRobo, xBola, yBola):
    return sqrt(((xBola - xRobo) ** 2) + ((yBola - yRobo) ** 2)
)

def calcularArctan(yRobo, xRobo):
   n = atan((5.18 - yRobo) / ( 5.08 - xRobo))

   return n

def grafico_trajetorias():
    x_bola = []
    y_bola = []
    x_robo = []
    y_robo = []

    for line in open("dados.txt", 'r'):
        t, x2, y2 = line.split()

        x_bola.append(float(x2))
        y_bola.append(float(y2))

    for line in open("pos_robo.txt", 'r'):
        t, x, y = line.split()
        x_robo.append(float(x))
        y_robo.append(float(y))

    plt.figure(figsize=(10, 6))
    plt.plot(x_bola, y_bola, label='Trajetória da Bola', color='red')
    plt.plot(x_robo, y_robo, label='Trajetória do Robô', color='blue')
    plt.xlabel("Eixo X")
    plt.ylabel('Eixo Y')
    plt.title("Gráfico das trajetórias da bola e do robô.")
    plt.grid(True)
    plt.legend()
    # Exiba o gráfico
    plt.show()

def trajetoria(x_robo, y_robo):
    x = 0
    t = 6.0
    n = calcularArctan(x_robo, y_robo)
    ax = 0.5 * cos(n)
    ay = 0.5 * sin(n)

    with open('pos_robo.txt', 'w+') as file:

        while (x < t):
            px = x_robo + ((ax * (x**2))/2)
            py = y_robo + ((ay * (x**2))/2)

            if py >= 5.18:
                py = 5.18
            if px >= 5.08:  
                px = 5.08

            file.write(f"{x:.2f} {px:.4f} {py:.4f}\n")
            x += 0.02

    grafico_trajetorias()

def velocidade_robo_bola_x(x_robo, y_robo):
    velocidade_x = []
    tempo = []
    velocidade_x_bola = []
    n = calcularArctan(y_robo, x_robo)
    ax = 0.6 * cos(n)
    ay = 0.6 * sin(n)
    t = 6
    x = 0
    v_inicial_x = 0
    v_inicial_y = 0
    with open("vel_robo.txt", 'w+') as file:
        while(x <= t):
            velo_x = v_inicial_x + (ax * x)
            velo_y = v_inicial_y + (ay * x)
            tempo.append(x)
            
            modulo = sqrt((velo_x**2) + (velo_y**2))
            if modulo >= 2.1:
                velo_x = 2.1 * cos(n)
                velo_y = 2.1 * sin(n)

            file.write(f"{x:.2f} {velo_x:.4f} {velo_y:.4f}\n")
            x += 0.02
    for lines in open("vel_robo.txt", 'r'):
        _, x_robo, _ = lines.split()
        velocidade_x.append(float(x_robo))
    for line in open("vel_bola.txt", 'r'):
        t, x_bola, __ = line.split()
        velocidade_x_bola.append(float(x_bola))
    
    plt.figure(figsize=(10, 6))
    plt.plot(tempo, velocidade_x_bola, label='Velocidade em x da bola', color='red')
    plt.xlabel("Tempo")
    plt.ylabel('Velocidade no eixo x')
    plt.title("Gráfico das componentes da velocidade em x")
    plt.plot(tempo, velocidade_x, label='Velocidade em x do robô', color='blue')
    plt.grid(True)
    plt.legend(fontsize='medium')
    # Exiba o gráfico
    plt.show()

def grafico_velocidade_y():
    velocidade_y = []
    velocidade_y_bola = []
    tempo = []
    for lines in open("vel_robo.txt", 'r'):
        _, __, y_robo = lines.split()
        velocidade_y.append(float(y_robo))
    for line in open("vel_bola.txt", 'r'):
        t, __, y_bola = line.split()
        tempo.append(float(t))
        velocidade_y_bola.append(float(y_bola))
        
    plt.figure(figsize=(10, 6))
    plt.plot(tempo, velocidade_y_bola, label='Velocidade em y da bola', color='red')
    plt.xlabel("Tempo")
    plt.ylabel('Velocidade no eixo y')
    plt.title("Gráfico das componentes da velocidade em y")
    plt.plot(tempo, velocidade_y, label='Velocidade em y do robô', color='blue')
    plt.grid(True)
    plt.legend(fontsize='medium')
    # Exiba o gráfico
    plt.show()

def calcular_acel(x1, x2):
    return (x2 - x1) / 0.02

def aceleracao_robo_x():
    dados = []
    tempo = []
    acel_bola_x = []
    acel_x = []
    with open("vel_robo.txt", "r") as arquivo:
        for linha in arquivo:
            t, x, __ = linha.split() 
            dados.append(float(x))
            
    for i in range(len(dados) - 1):
        x1 = dados[i]
        x2 = dados[i + 1]
        ax = float(calcular_acel(x1, x2))
        acel_x.append(ax)
    for line in open("acel_bola.txt", 'r'):
        t, x, y = line.split()
        tempo.append(float(t))
        acel_bola_x.append(float(x))
           
    tamanho_min = min(len(acel_x), len(acel_bola_x))
    tempo = list(range(tamanho_min))
        
    plt.figure(figsize=(10, 6))
    plt.plot(tempo, acel_bola_x[:tamanho_min], label='Aceleração da bola em X', color='red')
    plt.plot(tempo, acel_x[:tamanho_min], label='Aceleração do robô em X', color='blue')
    plt.xlabel("Tempo")
    plt.ylabel('Aceleração no eixo X')
    plt.title("Gráfico das acelerações no eixo X")
    plt.grid(True)
    plt.legend(fontsize='medium')
    # Exiba o gráfico
    plt.show()

def posicao_robo_bola_y():
    pos_y_robo = []
    pos_y_bola = []
    tempo = []
    
    for line in open("dados.txt", 'r'):
        t, x_bola, y_bola = line.split()
        t = float(t)
        t += 0.198
        pos_y_bola.append(float(y_bola))
        tempo.append(t)

       
    for line in open("pos_robo.txt", 'r'):
        t, x_robo, y_robo = line.split()
        pos_y_robo.append(float(y_robo))
    
    def grafico_y(pos_y_robo, pos_y_bola):
        plt.figure(figsize=(10, 6))
        plt.plot(tempo, pos_y_robo, label='Posição em Y do robô', color='blue')
        plt.plot(tempo, pos_y_bola, label='Posição em Y da bola', color='red')
        plt.xlabel("Tempo")
        plt.ylabel('Posição dos elementos no eixo Y')
        plt.title("Gráfico das coordenadas do robô e da bola no eixo Y em função do tempo")
        plt.grid(True)
        plt.legend()
        # Exiba o gráfico
        plt.show()
    
    grafico_y(pos_y_robo, pos_y_bola)
            
def posicao_robo_bola_x():
    pos_x_robo = []
    pos_x_bola = []
    tempo = []
    
    for line in open("dados.txt", 'r'):
        t, x_bola, y_bola = line.split()
        t = float(t)
        t += 0.198
        pos_x_bola.append(float(x_bola))
        tempo.append(t)

       
    for line in open("pos_robo.txt", 'r'):
        t, x_robo, y_robo = line.split()
        pos_x_robo.append(float(x_robo))
    
    def grafico_x(pos_x_robo, pos_x_bola):
        plt.figure(figsize=(10, 6))
        plt.plot(tempo, pos_x_robo, label='Posição em X do robô', color='blue')
        plt.plot(tempo, pos_x_bola, label='Posição em X da bola', color='red')
        plt.xlabel("Tempo")
        plt.ylabel('Posição dos elementos no eixo X')
        plt.title("Gráfico das coordenadas do robô e da bola no eixo X em função do tempo")
        plt.grid(True)
        plt.legend()
        # Exiba o gráfico
        plt.show()
        
    grafico_x(pos_x_robo, pos_x_bola)
    

def vel_robo(x_robo, y_robo):
    
    print("a")
    


def acel_robo(x_robo, y_robo):
      aceleracao_robo = 2  # m/s^2
      raio_interceptacao = 0.095  # 9.5 cm em m

      n = calcularArctan(y_robo, x_robo)
      # Lendo a trajetória da bola
      with open('dados.txt', 'r') as file:
          linhas = file.read().splitlines()

      with open('aceleracao_robo.txt', 'w+') as file:
        for linha in linhas[1:]:
            t, x_bola, y_bola = map(float, linha.split())

            # Calcular a distância entre o robô e um ponto da trajetória da bola.
            distancia_da_bola = distancia(x_robo, y_robo, x_bola, y_bola)

            # Calcular o tempo que o robô leva para percorrer essa distância.
            tempo_robo_atingir_bola = sqrt(
              (2 * distancia_da_bola) / aceleracao_robo)

            if t > 6:
                grafico_acel_robo()
                break
            else:
                # Calcular a nova posição do robô após t segundos
                new_x_robo = distancia_da_bola * cos(n)
                new_y_robo = distancia_da_bola * sin(n)

                file.write(f"{t} {new_x_robo:.4f} {new_y_robo:.4f}\n")         

def grafico_acel_robo():   
    ax_robo = []
    ay_robo = []
    for line in open("aceleracao_robo.txt", 'r'):
        tempo_robo, x, y = line.split()
        ax_robo.append(float(x))
        ay_robo.append(float(y))

    x_bola = []
    y_bola = []

    for line in open("dados.txt", 'r'):
        t, x2, y2 = line.split()
        x_bola.append(float(x2))
        y_bola.append(float(y2))

    plt.figure(figsize=(10, 6))
    plt.plot(ax_robo, ay_robo, label='Aceleração do Robô', color='blue')
    plt.plot(x_bola, y_bola, label='Aceleração da Bola', color='red')
    plt.xlabel("Componente ax")
    plt.ylabel('Componente ay')
    plt.title("Gráfico das componentes ax e ay da bola e do robô.")
    plt.grid(True)
    plt.legend()
    # Exiba o gráfico
    plt.show()



def grafico_robo_bola():
    x_robo = []
    y_robo = []
    for line in open("pos_robo.txt", 'r'):
        tempo_robo, x, y = line.split()
        x_robo.append(float(x))
        y_robo.append(float(y))

    plt.plot(x_robo, y_robo, label='Trajetória do Robô', color='blue')

    x_bola = []
    y_bola = []

    for line in open("dados.txt", 'r'):
        t, x2, y2 = line.split()
        x_bola.append(float(x2))
        y_bola.append(float(y2))

    plt.figure(figsize=(10, 6))
    plt.plot(x_bola, y_bola, label='Trajetória da Bola', color='red')
    plt.xlabel("Eixo X")
    plt.ylabel('Eixo Y')
    plt.title("Gráfico das trajetórias da bola e do robô até a interceptação.")
    plt.grid(True)
    plt.legend()

    # Exiba o gráfico
    plt.show()
    
def distancia_robo_bola():
    tempo = []
    dist = []
    with open("pos_robo.txt", 'r') as arq1, open("dados.txt", 'r') as arq2:
        for l1, l2 in zip(arq1, arq2):
            valores_robo = l1.split()
            valores_bola = l2.split()
            x_robo = float(valores_robo[1])
            y_robo = float(valores_robo[2])
            x_bola = float(valores_bola[1])
            y_bola = float(valores_bola[2])
            x = x_robo - x_bola
            y = y_robo - y_bola
            modulo = sqrt((x**2) + (y**2))
            dist.append(modulo)
        for line in open("dados.txt", 'r'):
            t, temp1, temp2 = line.split()
            t = float(t)
            tempo.append(t)
            t += 0.098
            
            
    plt.figure(figsize=(10, 6))
    plt.plot(tempo, dist, color='blue')
    plt.xlabel("Tempo")
    plt.ylabel('Distância')
    plt.title("Distância relativa entre o robô e a bola.")
    plt.grid(True)
    # Exiba o gráfico
    plt.show()
    
