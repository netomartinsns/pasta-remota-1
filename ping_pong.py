import pygame
import sys
import time
import math

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da bola
ball_speed = [3, 3]
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

#variaveis do contador
player1_score = 0
player2_score = 0
a = player2_score
b = player1_score
# Configurações das raquetes
paddle_speed = 6
paddle1 = pygame.Rect(10, HEIGHT // 2 - 60, 10, 120)
paddle2 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 60, 10, 120)

# Função para desenhar os elementos na tela
def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.flip()
    

# Função principal do jogo
def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1.top > 0:
            paddle1.y -= paddle_speed
        if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
            paddle1.y += paddle_speed
        if keys[pygame.K_UP] and paddle2.top > 0:
            paddle2.y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
            paddle2.y += paddle_speed

        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] = -ball_speed[1]
        if ball.left <= 0 or ball.right >= WIDTH:
          ball_speed[0] = -ball_speed[0]
        if ball.left <= 0 or ball.left >= WIDTH:
         global a
         a += 1
         print(a)
        if ball.right <= 0 or ball.right >= WIDTH:
         global b
         b += 1
         print(b)
         
         
         
         
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed[0] = -ball_speed[0]

        draw()
        clock.tick(60)
        

if __name__ == "__main__":
    main()

#LEMBRETE QUE PARA O JOGADOR 1 É W PARA CIMA E S PARA BAIXO E PARA O JOGADOR 2 É A SETA PARA CIMA E PARA BAIXO

#ESTE É UM JOGO SIMPLES DE PING PONG FEITO EM PYTHON COM A BIBLIOTECA PYGAME

#PARA RODAR O JOGO É NECESSÁRIO TER O PYGAME INSTALADO, CASO NÃO TENHA INSTALADO, INSTALE COM O COMANDO pip install pygame

#JOGO AINDA NÃO FINALIZADO, FALTA ADICIONAR O SISTEMA DE PONTUAÇÃO E O SISTEMA DE VITÓRIA

#AGORA AGUARDANDO MEU FILHO BERNARDO PARA AJUSTAR O JOGO