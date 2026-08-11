import pygame
from pygame.locals import *
from sys import exit
pygame.init() 
largura = 640
altura = 480
x = largura / 2
y = altura / 2

pygame.display.set_caption("Primeiro Jogo do KAYKY")
#esse while é para o jogo não fechar, e ficar rodando.
relogio = pygame.time.Clock()
#esse relogio é para o jogo não ficar rodando muito rápido, e ficar mais lento.
tela = pygame.display.set_mode((largura, altura))
#esse tela é para criar a tela do jogo, e colocar o tamanho da tela.
while True:
#esse while é para o jogo não fechar, e ficar rodando.
    relogio.tick(60)
    tela.fill((6, 0, 0))
    #esse fill é para colocar a cor de fundo da tela, e o (6, 0, 0) é a cor de fundo da tela. 
    pygame.display.update()
    #esse update é para atualizar a tela do jogo, e mostrar as mudanças na tela.
    for event in pygame.event.get():
     #esse for é para pegar os eventos do jogo, e verificar se o jogador clicou no X para fechar o jogo.
       if event.type == KEYDOWN:
        #esse if é para verificar se a tecla foi pressionada, e o KEYDOWN é para verificar se a tecla foi pressionada.
        
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
    #esse if é para quando a tecla for pressionada, .

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