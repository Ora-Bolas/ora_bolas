import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da tela
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# Defina as cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Defina as velocidades iniciais para a bola e o robô
BALL_SPEED = 5
ROBOT_SPEED = 3

# Defina a classe Ball
class Ball:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed

# Defina a classe Robot
class Robot:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x -= self.speed

# Função principal
def main():
    # Crie a tela
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bola e Robô")

    # Crie objetos Ball e Robot
    ball = Ball(50, SCREEN_HEIGHT // 2, 20, RED, BALL_SPEED)
    robot = Robot(SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2 - 50, 50, 100, BLUE, ROBOT_SPEED)

    clock = pygame.time.Clock()

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimente a bola e o robô
        ball.move()
        robot.move()

        # Limpe a tela
        screen.fill(WHITE)

        # Desenhe a bola e o robô
        ball.draw(screen)
        robot.draw(screen)

        # Atualize a tela
        pygame.display.flip()

        # Defina o limite de frames por segundo
        clock.tick(60)

        # Verifique se a bola e o robô se interceptam
        if (robot.x <= ball.x + ball.radius <= robot.x + robot.width and
            robot.y <= ball.y <= robot.y + robot.height):
            print("Interceptado!")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
