import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Primeiro Jogo do KAYKY")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    tela.fill((6, 1, 0))
    pygame.display.update()

    pygame.draw.rect(tela, (255, 0, 0), (200, 365, 50, 50))

    pygame.draw.circle(tela, (0, 255, 0), (330, 375), 40)


    pygame.draw.line(tela, (255, 255, 0), (1, 450), (690, 450 ), 70)

    pygame.display.update()