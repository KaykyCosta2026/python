import pygame
from pygame.locals import *
from sys import exit
pygame.init() 
largura = 640
altura = 480
x = largura / 2
y = altura / 2
pygame.display.set_caption("Primeiro Jogo do KAYKY")
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
while True:
    relogio.tick(60)
    tela.fill((6, 0, 0))
    pygame.display.update()
    for event in pygame.event.get():
       if event.type == KEYDOWN:
                if event.key == K_a:
                    x = x - 10
                elif event.key == K_d:
                    x = x + 10
                elif event.key == K_w:
                    y = y - 10
                elif event.key == K_s:
                    y = y + 10
    if event.type == QUIT:
        exit()
    if pygame .key.get_pressed()[K_a]:
            x = x - 10
    if pygame .key.get_pressed()[K_d]:
            x = x + 10
    if pygame .key.get_pressed()[K_w]:
            y = y - 10
    if pygame .key.get_pressed()[K_s]:
            y = y + 10
                 
    pygame.draw.rect(tela, (255, 80, 80), (x, y, 50, 50), 30)
    pygame.display.update()