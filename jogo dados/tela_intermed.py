import pygame
from pygame.locals import *
from pygame import *

pygame.init()

TAMANHO = (1000, 800)
screen = pygame.display.set_mode(TAMANHO)
FPS = 60
clock = pygame.time.Clock()

fundo = pygame.image.load('assets/fundo.webp')
fundo = pygame.transform.scale(fundo, TAMANHO)

botao_verde = pygame.image.load('assets/botao_verde.png')
botao_verde = pygame.transform.scale(botao_verde, (250, 250))
botao_verde_rect = botao_verde.get_rect(topleft=(200, 550))

botao_vermelho = pygame.image.load('assets/botao_vermelho.png')
botao_vermelho = pygame.transform.scale(botao_vermelho, (250, 250))
botao_vermelho_rect = botao_vermelho.get_rect(topright=(800, 550))

fonte = pygame.font.Font('assets/fontt/Pixeltype.ttf', 45)
fonte_titulo = pygame.font.Font('assets/fontt/casino-font/GrandcasinoRegular-mLExx.otf', 80)

titulo1 = fonte_titulo.render('Voce deseja', True, (0, 0, 0))
titulo2 = fonte_titulo.render('apostar seus pontos?', True, (0, 0, 0))
texto_verde = fonte.render('apostar', True, (0, 0, 0))
texto_vermelho = fonte.render('sair', True, (0, 0, 0))

titulo_rect1 = titulo1.get_rect(center=(TAMANHO[0] // 2, 50))
titulo_rect2 = titulo2.get_rect(center=(TAMANHO[0] // 2, 150))
texto_verde_rect = texto_verde.get_rect(center=botao_verde_rect.center)
texto_vermelho_rect = texto_vermelho.get_rect(center=botao_vermelho_rect.center)

rodando = True
while rodando:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            rodando = False
        
        if ev.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if botao_verde_rect.collidepoint(mouse_pos):
                    print('colisao azul')
                elif botao_vermelho_rect.collidepoint(mouse_pos):
                    print('colisao vermelho')

    screen.fill('White')

    screen.blit(fundo, (0, 0))  


    screen.blit(titulo1, titulo_rect1)
    screen.blit(titulo2, titulo_rect2)
    screen.blit(botao_verde, botao_verde_rect)
    screen.blit(botao_vermelho, botao_vermelho_rect)

    screen.blit(texto_verde, texto_verde_rect)
    screen.blit(texto_vermelho, texto_vermelho_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
