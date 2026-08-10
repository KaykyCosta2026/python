import pygame                              
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura / 2
y = altura / 2
pygame.display.set_caption("Primeiro jogo com Pygame")
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
x_azul = randint(40, 600)
y_azul = randint(50, 430)



while True:
    relogio.tick(25)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 5
            elif event.key == K_d:
                x = x + 5
            elif event.key == K_w:
                y = y - 5
            elif event.key == K_s:
                y = y + 5
        if event.type == QUIT:
            exit()

    if pygame.key.get_pressed()[K_a]:
        x = x - 5
    if pygame.key.get_pressed()[K_d]:
        x = x + 5
    if pygame.key.get_pressed()[K_w]:
        y = y - 5
    if pygame.key.get_pressed()[K_s]:
        y = y + 5

    ret_vermelho=pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_azul=pygame.draw.rect(tela, (0, 255, 0), (x_azul, y_azul, 40, 50))
    pygame.draw.rect(tela, (255, 80, 80), (x, y, 40, 50), 3)
    # Verificar colisão entre os retângulos

    if ret_vermelho.colliderect(ret_azul):
        #print("Colisão detectada!")
    
      

   # if y >= altura:
   #     y = 0

   # y = y + 5 
     pygame.display.update()