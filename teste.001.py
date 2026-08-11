import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# Configurações da tela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha - Retângulos em Grade")

# Tamanho de cada bloco (retângulo)
TAMANHO_BLOCO = 20

# Fonte e Pontuação
fonte = pygame.font.SysFont(None, 36)
pontos = 0

# Posição inicial da cabeça (alinhada à grade)
x = (largura // 2) // TAMANHO_BLOCO * TAMANHO_BLOCO
y = (altura // 2) // TAMANHO_BLOCO * TAMANHO_BLOCO

# Direção inicial (dx, dy)
velocidade_x = TAMANHO_BLOCO
velocidade_y = 0

# Lista para guardar todos os blocos do corpo
lista_cobra = []
comprimento_inicial = 3

# Posição do objetivo/comida (alinhada à grade)
x_azul = randint(0, (largura - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
y_azul = randint(0, (altura - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO

relogio = pygame.time.Clock()

def desenha_cobra(lista_corpo):
    """Desenha cada retângulo do corpo com uma borda para destacar os blocos."""
    for pos in lista_corpo:
        # Desenha o retângulo do corpo
        pygame.draw.rect(tela, (255, 0, 0), (pos[0], pos[1], TAMANHO_BLOCO, TAMANHO_BLOCO))
        # Desenha uma borda preta em cada bloco para separá-los visualmente
        pygame.draw.rect(tela, (0, 0, 0), (pos[0], pos[1], TAMANHO_BLOCO, TAMANHO_BLOCO), 1)

while True:
    # Ajusta a velocidade do jogo (quadros por segundo)
    relogio.tick(10)
    tela.fill((0, 0, 0))

    # Exibe a pontuação
    texto = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    tela.blit(texto, (10, 10))

    # Captura os eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Altera a direção ao pressionar as teclas (evitando que ela volte contra si mesma)
        if event.type == KEYDOWN:
            if (event.key == K_a or event.key == K_LEFT) and velocidade_x == 0:
                velocidade_x = -TAMANHO_BLOCO
                velocidade_y = 0
            elif (event.key == K_d or event.key == K_RIGHT) and velocidade_x == 0:
                velocidade_x = TAMANHO_BLOCO
                velocidade_y = 0
            elif (event.key == K_w or event.key == K_UP) and velocidade_y == 0:
                velocidade_x = 0
                velocidade_y = -TAMANHO_BLOCO
            elif (event.key == K_s or event.key == K_DOWN) and velocidade_y == 0:
                velocidade_x = 0
                velocidade_y = TAMANHO_BLOCO

    # Atualiza a posição da cabeça avançando em blocos
    x += velocidade_x
    y += velocidade_y

    # Adiciona a nova posição da cabeça ao corpo
    cabeca_cobra = [x, y]
    lista_cobra.append(cabeca_cobra)

    # Mantém a cobra no tamanho correto removendo a cauda antiga
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    # Objetos Rect para colisão
    ret_cabeca = pygame.Rect(x, y, TAMANHO_BLOCO, TAMANHO_BLOCO)
    ret_comida = pygame.Rect(x_azul, y_azul, TAMANHO_BLOCO, TAMANHO_BLOCO)

    # Desenha a cobra e o retângulo da comida
    desenha_cobra(lista_cobra)
    pygame.draw.rect(tela, (0, 255, 0), ret_comida)

    # Colisão com a comida
    if ret_cabeca.colliderect(ret_comida):
        x_azul = randint(0, (largura - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
        y_azul = randint(0, (altura - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
        pontos += 1
        comprimento_inicial += 1  # Adiciona exatamente +1 bloco de retângulo ao corpo

    # Colisão com as bordas da tela
    if x < 0 or x >= largura or y < 0 or y >= altura:
        pygame.quit()
        exit()

    pygame.display.update()