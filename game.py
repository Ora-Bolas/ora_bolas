import pygame
import sys

def ler_posicoes_arquivo(nome_arquivo):
    try:
        posicoes_x = []
        posicoes_y = []
        with open(nome_arquivo, 'r') as arquivo:
            for line in arquivo:
                _, x, y = line.split()
                posicoes_x.append(float(x)/10)
                posicoes_y.append(float(y)/10)
        return posicoes_x, posicoes_y
    except FileNotFoundError:
        print("Arquivo não encontrado:", nome_arquivo)
        return [], []
    except ValueError:
        print("Erro ao ler os dados do arquivo:", nome_arquivo)
        return [], []

def animar():
    pygame.init()

    # Define as dimensões do campo
    LARGURA_CAMPO, ALTURA_CAMPO = 900, 600

    # Define as dimensões da tela
    LARGURA_TELA, ALTURA_TELA = LARGURA_CAMPO, ALTURA_CAMPO

    # Define as margens
    MARGEM_ESQUERDA = (LARGURA_TELA - LARGURA_CAMPO) // 2
    MARGEM_SUPERIOR = (ALTURA_TELA - ALTURA_CAMPO) // 2

    # Define as cores
    BRANCO = (255, 255, 255)
    VERDE = (0, 128, 0)

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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Preenche o fundo com a cor verde
        tela.fill(VERDE)

        # Desenha o campo
        pygame.draw.rect(tela, BRANCO, (MARGEM_ESQUERDA, MARGEM_SUPERIOR, LARGURA_CAMPO, ALTURA_CAMPO), 2)
        pygame.draw.line(tela, BRANCO, (MARGEM_ESQUERDA + LARGURA_CAMPO // 2, MARGEM_SUPERIOR),
                         (MARGEM_ESQUERDA + LARGURA_CAMPO // 2, MARGEM_SUPERIOR + ALTURA_CAMPO), 2)
        pygame.draw.rect(tela, BRANCO, (MARGEM_ESQUERDA, MARGEM_SUPERIOR + (ALTURA_CAMPO // 2) - 50, 50, 100), 5)
        pygame.draw.rect(tela, BRANCO, (MARGEM_ESQUERDA + LARGURA_CAMPO - 50, MARGEM_SUPERIOR + (ALTURA_CAMPO // 2) - 50, 50, 100), 5)
        pygame.draw.circle(tela, BRANCO, (MARGEM_ESQUERDA + LARGURA_CAMPO // 2, MARGEM_SUPERIOR + ALTURA_CAMPO // 2), 75, 2)

        # Desenha os objetos na tela
        if indice_atual < len(posicoes_robo_x):
            x_robo = MARGEM_ESQUERDA + posicoes_robo_x[indice_atual] * (LARGURA_CAMPO - 20)
            y_robo = MARGEM_SUPERIOR + (1 - posicoes_robo_y[indice_atual]) * (ALTURA_CAMPO - 20)
            pygame.draw.circle(tela, BRANCO, (int(x_robo), ALTURA_TELA - int(y_robo)), 10)
        if indice_atual < len(posicoes_bola_x):
            x_bola = MARGEM_ESQUERDA + posicoes_bola_x[indice_atual] * (LARGURA_CAMPO - 20)
            y_bola = MARGEM_SUPERIOR + (1 - posicoes_bola_y[indice_atual]) * (ALTURA_CAMPO - 20)
            pygame.draw.circle(tela, BRANCO, (int(x_bola), ALTURA_TELA - int(y_bola)), 7)

        # Atualiza a tela
        pygame.display.flip()

        # Atualiza o índice para o próximo frame
        indice_atual += 1

        # Define o limite de frames por segundo
        clock.tick(60)

        # Verifica se todos os frames foram exibidos
        if indice_atual >= max(len(posicoes_robo_x), len(posicoes_bola_x)):
            break
