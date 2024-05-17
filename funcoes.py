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

    for line in open("trajetoria_bola.txt", 'r'):
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
    plt.xlabel("Eixo X (m)")
    plt.ylabel('Eixo Y (m)')
    plt.title("Gráfico das trajetórias da bola e do robô. (m)")
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
    ax = 0.5 * cos(n)
    ay = 0.5 * sin(n)
    t = 6
    x = 0
    v_inicial_x = 0
    v_inicial_y = 0
    with open("vel_robo.txt", 'w+') as file:
        while(x <= t):
            velo_x = v_inicial_x + (ax * x)
            velo_y = v_inicial_y + (ay * x)
            modulo = sqrt((velo_x**2) + (velo_y**2))
            if modulo >= 1.9:
                while x < 6:
                    velo_x = velo_x - 0.072
                    velo_y = velo_y - 0.072
                    x += 0.02
                    if velo_x <= 0 or velo_y <= 0:
                        velo_x = 0
                        velo_y = 0
                    file.write(f"{x:.2f} {velo_x:.4f} {velo_y:.4f}\n")
            else:
                file.write(f"{x:.2f} {velo_x:.4f} {velo_y:.4f}\n")
                x += 0.02
                
    for lines in open("vel_robo.txt", 'r'):
        t, x_robo, _ = lines.split()
        velocidade_x.append(float(x_robo))
        tempo.append(float(t))
    for line in open("vel_bola.txt", 'r'):
        __, x_bola, __ = line.split()
        velocidade_x_bola.append(float(x_bola))
    
    plt.figure(figsize=(10, 6))
    plt.plot(tempo, velocidade_x_bola, label='Velocidade em x da bola', color='red')
    plt.xlabel("Tempo (s)")
    plt.ylabel('Velocidade no eixo x (m/s)')
    plt.title("Gráfico das componentes da velocidade em x (m/s)")
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
    plt.xlabel("Tempo (s)")
    plt.ylabel('Velocidade no eixo y (m/s)')
    plt.title("Gráfico das componentes da velocidade em y (m/s)")
    plt.plot(tempo, velocidade_y, label='Velocidade em y do robô', color='blue')
    plt.grid(True)
    plt.legend(fontsize='medium')
    # Exiba o gráfico
    plt.show()

def calcular_aceleracao(v1, v2, t1, t2):
    delta_v = v2 - v1
    delta_t = t2 - t1
    if delta_t != 0:
        return delta_v / delta_t
    else:
        return 0

def aceleracao_robo_x():
    velocidades_robo = []
    tempo = []
    aceleracao_robo = []
    acel_bola_x = []

    for line in open("acel_bola.txt", 'r'):
            t, x, y = line.split()
            tempo.append(float(t))
            acel_bola_x.append(float(x))
            
    with open("vel_robo.txt", "r") as arquivo:
        for linha in arquivo:
            t, v_robo, _ = linha.split()
            velocidades_robo.append(float(v_robo))

    for i in range(len(velocidades_robo) - 1):
        v1 = velocidades_robo[i]
        v2 = velocidades_robo[i + 1]
        t1 = tempo[i]
        t2 = tempo[i + 1]
        acel_robo = calcular_aceleracao(v1, v2, t1, t2)
        aceleracao_robo.append(acel_robo)
    
    plt.figure(figsize=(10, 6))
    plt.plot(tempo[:-1], aceleracao_robo, label='Aceleração do robô em X', color='blue')
    plt.plot(tempo, acel_bola_x, label='Aceleração da bola em X', color='red')
    plt.xlabel("Tempo (s)")
    plt.ylabel('Aceleração no eixo X (m/s^2)')
    plt.title("Gráfico da aceleração do robô em relação ao tempo (m/s^2)")
    plt.grid(True)
    plt.legend(fontsize='medium')
    plt.show()

def aceleracao_robo_y():
    velocidades_robo = []
    tempo = []
    aceleracao_robo = []
    acel_bola_y = []
    
    with open("vel_robo.txt", "r") as arquivo:
        for linha in arquivo:
            t, _, v_robo = linha.split()
            tempo.append(float(t))
            velocidades_robo.append(float(v_robo))
            
    for i in range(len(velocidades_robo) - 1):
        v1 = velocidades_robo[i]
        v2 = velocidades_robo[i + 1]
        t1 = tempo[i]
        t2 = tempo[i + 1]
        acel_robo = calcular_aceleracao(v1, v2, t1, t2)
        aceleracao_robo.append(acel_robo)
    
    for line in open("acel_bola.txt", 'r'):
            t, x, y = line.split()
            acel_bola_y.append(float(y))

    plt.figure(figsize=(10, 6))
    plt.plot(tempo[:-1], aceleracao_robo, label='Aceleração do robô em Y', color='blue')
    plt.plot(tempo, acel_bola_y, label='Aceleração da bola em Y', color='red')
    plt.xlabel("Tempo (s)")
    plt.ylabel('Aceleração no eixo Y (m/s^2)')
    plt.title("Gráfico da aceleração do robô no eixo Y em relação ao tempo (m/s^2)")
    plt.grid(True)
    plt.legend(fontsize='medium')
    plt.show()

def posicao_robo_bola_y():
    pos_y_robo = []
    pos_y_bola = []
    tempo = []
    
    for line in open("trajetoria_bola.txt", 'r'):
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
        plt.xlabel("Tempo (s)")
        plt.ylabel('Posição dos elementos no eixo Y (m)')
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
    
    for line in open("trajetoria_bola.txt", 'r'):
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
        plt.xlabel("Tempo (s)")
        plt.ylabel('Posição dos elementos no eixo X (m)')
        plt.title("Gráfico das coordenadas do robô e da bola no eixo X em função do tempo")
        plt.grid(True)
        plt.legend()
        # Exiba o gráfico
        plt.show()
        
    grafico_x(pos_x_robo, pos_x_bola)
    
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

    for line in open("trajetoria_bola.txt", 'r'):
        t, x2, y2 = line.split()
        x_bola.append(float(x2))
        y_bola.append(float(y2))

    plt.figure(figsize=(10, 6))
    plt.plot(x_bola, y_bola, label='Trajetória da Bola', color='red')
    plt.xlabel("Eixo X (m)")
    plt.ylabel('Eixo Y (m)')
    plt.title("Gráfico das trajetórias da bola e do robô até a interceptação.")
    plt.grid(True)
    plt.legend()

    # Exiba o gráfico
    plt.show()
    
def distancia_robo_bola():
    tempo = []
    dist = []
    with open("pos_robo.txt", 'r') as arq1, open("trajetoria_bola.txt", 'r') as arq2:
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
        for line in open("trajetoria_bola.txt", 'r'):
            t, temp1, temp2 = line.split()
            t = float(t)
            tempo.append(t)
            
            
    plt.figure(figsize=(10, 6))
    plt.plot(tempo, dist, color='blue')
    plt.xlabel("Tempo (s)")
    plt.ylabel('Distância (m)')
    plt.title("Distância relativa entre o robô e a bola.")
    plt.grid(True)
    # Exiba o gráfico
    plt.show()
    
