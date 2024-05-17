import pygame
import sys

def ler_posicoes_arquivo(nome_arquivo):
    try:
        posicoes_x = []
        posicoes_y = []
        with open(nome_arquivo, 'r') as arquivo:
            for line in arquivo:
                _, x, y = line.split()
                posicoes_x.append(float(x) / 10)
                posicoes_y.append(float(y) / 10)
        return posicoes_x, posicoes_y
    except FileNotFoundError:
        print("Arquivo não encontrado:", nome_arquivo)
        return [], []
    except ValueError:
        print("Erro ao ler os dados do arquivo:", nome_arquivo)
        return [], []

def draw_field(window, width, height):
    green = (0, 128, 0)
    white = (255, 255, 255)

    window.fill(green)
    pygame.draw.line(window, white, (width // 2, 0), (width // 2, height), 5)
    pygame.draw.circle(window, white, (width // 2, height // 2), 70, 5)
    pygame.draw.circle(window, white, (width // 2, height // 2), 8)

    # Desenhar as áreas do campo de futebol
    pygame.draw.rect(window, white, (0, height // 2 - 50, 50, 100), 5)
    pygame.draw.rect(window, white, (width - 50, height // 2 - 50, 50, 100), 5)

def animar():
    pygame.init()

    # Define as dimensões do campo
    LARGURA_CAMPO, ALTURA_CAMPO = 900, 600

    # Define as dimensões da tela
    LARGURA_TELA, ALTURA_TELA = LARGURA_CAMPO, ALTURA_CAMPO

    # Define as cores
    BRANCO = (255, 255, 255)
    PRETO = (0,0,0)

    # Cria a tela
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Animação de Bola e Robô')

    # Carrega as posições do robô e da bola
    posicoes_robo_x, posicoes_robo_y = ler_posicoes_arquivo("pos_robo.txt")
    posicoes_bola_x, posicoes_bola_y = ler_posicoes_arquivo("trajetoria_bola.txt")

    # Define o índice inicial
    indice_atual = 0

    clock = pygame.time.Clock()

    # Loop principal do jogo
    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        # Desenha o campo de futebol
        draw_field(tela, LARGURA_TELA, ALTURA_TELA)

        # Desenha os objetos na tela
        if indice_atual < len(posicoes_robo_x):
            x_robo = (posicoes_robo_x[indice_atual] * 1000) * (LARGURA_TELA / LARGURA_CAMPO)
            y_robo = ALTURA_TELA - (posicoes_robo_y[indice_atual] * 1000) * (ALTURA_TELA / ALTURA_CAMPO)
            pygame.draw.circle(tela, PRETO, (int(x_robo), int(y_robo)), 8)
        if indice_atual < len(posicoes_bola_x):
            x_bola = (posicoes_bola_x[indice_atual] * 1000) * (LARGURA_TELA / LARGURA_CAMPO)
            y_bola = ALTURA_TELA - (posicoes_bola_y[indice_atual] * 1000) * (ALTURA_TELA / ALTURA_CAMPO)
            pygame.draw.circle(tela, BRANCO, (int(x_bola), int(y_bola)), 5)

        # Atualiza a tela
        pygame.display.flip()

        # Atualiza o índice para o próximo frame
        indice_atual += 1

        # Define o limite de frames por segundo
        clock.tick(60)

        # Verifica se todos os frames foram exibidos
        if indice_atual >= max(len(posicoes_robo_x), len(posicoes_bola_x)):
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    animar()
