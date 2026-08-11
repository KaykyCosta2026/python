
import pygame
from pygame.locals import *
from sys import exit
from random import randint
pontos =  str(0) 
texto = "Pontos: " + str(pontos)

branco = (255, 255, 255)

pygame.init()

# Configurações da tela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Primeiro jogo com Pygame")

# Posições e variáveis do jogador (Vermelho)
x = largura / 2
y = altura / 2
largura_ret = 40
altura_ret = 50

# Posições do objetivo (Azul/Verde)
x_azul = randint(40, 600)
y_azul = randint(50, 430)

relogio = pygame.time.Clock()

while True:
    fonte = pygame.font.SysFont(None,48)
    texto = fonte.render("Pontos: " + str(pontos), True, (255, 255, 255))
    tela.fill((0, 0, 0))                         
    tela.blit(texto, (10, 10))
    relogio.tick(25)
     
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Movimentação contínua e suave do jogador
    teclas = pygame.key.get_pressed()
    if teclas[K_a]:
        x -= 5
    if teclas[K_d]:
        x += 5
    if teclas[K_w]:
        y -= 5
    if teclas[K_s]:
        y += 5

    # Desenho dos elementos na tela
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, largura_ret, altura_ret))
    ret_azul = pygame.draw.rect(tela, (0, 255, 0), (x_azul, y_azul, 40, 50))
    pygame.draw.rect(tela, (255, 80, 80), (x, y, largura_ret, altura_ret), 3)
    
    
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = str(int(pontos) + 1)
    # 2. Colisão com as bordas da tela: Fecha o programa
    if x < 0 or x + largura_ret > largura or y < 0 or y + altura_ret > altura:
        pygame.quit()
        exit()

    pygame.display.update()