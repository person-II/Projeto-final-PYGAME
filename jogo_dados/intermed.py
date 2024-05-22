import pygame
from pygame import *


init()

TAMANHO2 = (1000, 800)
screen = display.set_mode(TAMANHO2)
FPS = 60
relogio = time.Clock()

fundo = image.load('assets/fundo.webp')
fundo = transform.scale(fundo, TAMANHO2)

botao_verde = image.load('assets/botao_verde.png')
botao_verde = transform.scale(botao_verde, (250, 250))
botao_verde_rect = botao_verde.get_rect(topright=(800, 550))

botao_vermelho = image.load('assets/botao_vermelho.png')
botao_vermelho = transform.scale(botao_vermelho, (250, 250))
botao_vermelho_rect = botao_vermelho.get_rect(topleft=(200, 550))

fonte = font.Font('assets/fontt/fight-night-font/FightNight-w9V3.ttf', 35)
fonte2 = font.Font('assets/fontt/fight-night-font/FightNight-w9V3.ttf', 30)
fonte_titulo = font.Font('assets/fontt/casino-font/GrandcasinoRegular-mLExx.otf', 80)

titulo1 = fonte_titulo.render('Voce deseja', True, 'Black')
titulo2 = fonte_titulo.render('apostar seus pontos ?', True, 'Black')

texto_verde = fonte2.render('APOSTAR', True, 'Black')
texto_vermelho = fonte.render('SAIR', True, 'Black')

titulo_rect1 = titulo1.get_rect(center=(TAMANHO2[0] // 2, 50))
titulo_rect2 = titulo2.get_rect(center=(TAMANHO2[0] // 2, 150))

texto_vermelho_rect = texto_vermelho.get_rect(center=(botao_vermelho_rect.center[0] - 8, 690))
texto_verde_rect = texto_verde.get_rect(center=(botao_verde_rect.center[0] - 4, 690))

# rodando = True
# while rodando:
#     for ev in event.get():
#         if ev.type == QUIT:
#             rodando = False
        
#         if ev.type == MOUSEBUTTONDOWN:
#             if mouse.get_pressed()[0]:
#                 mouse_pos = mouse.get_pos()
#                 if botao_verde_rect.collidepoint(mouse_pos):
#                     main.BACK_BO = True
#                 elif botao_vermelho_rect.collidepoint(mouse_pos):
#                     print('colisao sair')

#     screen.fill('White')

#     screen.blit(fundo, (0, 0))  

#     screen.blit(titulo1, titulo_rect1)
#     screen.blit(titulo2, titulo_rect2)
#     screen.blit(botao_verde, botao_verde_rect)
#     screen.blit(botao_vermelho, botao_vermelho_rect)

#     screen.blit(texto_verde, texto_verde_rect)
#     screen.blit(texto_vermelho, texto_vermelho_rect)

#     display.update()
#     clock.tick(FPS)

# pygame.quit()


def tela_intermed():
    display.set_mode((1000, 800))
    rodando = True
    while rodando:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                rodando = False
                return 'exit'  # Return a string to indicate exit
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    if botao_verde_rect.collidepoint(mouse_pos):
                        return 'bet'  # Continue to back bo game
                    elif botao_vermelho_rect.collidepoint(mouse_pos):
                        return 'exit'  # Exit the game

        screen.fill('White')
        screen.fill('White')
        screen.blit(fundo, (0, 0))
        screen.blit(titulo1, titulo_rect1)
        screen.blit(titulo2, titulo_rect2)
        screen.blit(botao_verde, botao_verde_rect)
        screen.blit(botao_vermelho, botao_vermelho_rect)
        screen.blit(texto_verde, texto_verde_rect)
        screen.blit(texto_vermelho, texto_vermelho_rect)

        pygame.display.update()
        relogio.tick(FPS)

