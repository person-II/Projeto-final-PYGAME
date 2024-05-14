from pygame import *
import pygame
from random import randint
import json

init()

# * CONSTANTES
TAMANHO = (500, 600)
FPS = 60

# * JANELA E CLOCK
screen = display.set_mode(TAMANHO)
clock = time.Clock()
display.set_caption('dado')

# * FONTES
my_font = font.SysFont('OpensSans-Regular', 30)
my_font2 = font.SysFont('OpensSans-Regular', 25)
my_font3 = font.SysFont('OpensSans-Regular', 15)

# * SUPERFICIES / IMAGENS ...
jogando = my_font.render('jogando dados...', False, 'Black')
jogando_rect = jogando.get_rect(center=(250, 100))

victory = my_font.render('VITORIA', False, 'Black')
defeat = my_font.render('DERROTA', False, 'Black')
tie = my_font.render('EMPATE', False, 'Black')
vic_rect = victory.get_rect(center=(250, 150))
def_rect = defeat.get_rect(center=(250, 150))
tie_rect = tie.get_rect(center=(250, 150))

rect_ver = Surface((100, 65))
rect_ver.fill('Red')
rect_ver = rect_ver.get_rect(topleft=(275, 270))
rect_az = Surface((100, 65))
rect_az.fill('Blue')
rect_az = rect_az.get_rect(topleft=(125, 270))

play_again = my_font2.render('pressione espaço para', False, 'Black')
play_again2 = my_font2.render('jogar novamente', False, 'Black')
again_rect = play_again.get_rect(center=(250, 480))
again2_rect = play_again2.get_rect(center=(250, 505))

moeda5 = Surface((60, 60))
moeda10 = Surface((70, 70))
moeda20 = Surface((85, 85))
rect5 = moeda5.get_rect(midleft=(95, 400))
rect10 = moeda10.get_rect(midleft=(180, 400))
rect20 = moeda20.get_rect(midleft=(270, 400))
moeda5_txt = my_font.render('5', False, 'Black')
moeda10_txt = my_font.render('10', False, 'Black')
moeda20_txt = my_font.render('20', False, 'Black')
txt_5_rect = moeda5_txt.get_rect(midleft=(117, 400))
txt_10_rect = moeda10_txt.get_rect(midleft=(195, 400))
txt_20_rect = moeda20_txt.get_rect(midleft=(294, 400))

rect_allwin = Surface((70,45))
rect_allwin = rect_allwin.get_rect(midleft=(380, 400))
allwin_txt = my_font3.render('ALL WIN', False, 'Black')
allwin_txt_rect = allwin_txt.get_rect(midleft=(385, 400))

# * CAIXA DE TEXTO - USERNAME
username = ''
input_rect = Rect(100, 545, 140, 40)
color_active = Color('Light Gray')
color_passive = Color('lightskyblue3')
colorr = color_passive
type_active = False


# * VARIAVEIS
PONTOS_INICIAIS = 100
clicou = False
bet = True
Draw = True
placed_bet = False
aposta = 0

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
        
        if ev.type == MOUSEBUTTONDOWN:
            if input_rect.collidepoint(ev.pos):
                type_active = True
            else:
                type_active = False

        if ev.type == KEYDOWN:
            if type_active:
                if ev.key == K_BACKSPACE:
                    username = username[:-1]
                elif ev.key == K_RETURN:
                    done_username = True
                else:
                    username += ev.unicode
    
    if type_active:
        colorr = color_active
    else:
        colorr = color_passive
    screen.fill((94, 129, 162))
    draw.rect(screen, colorr, input_rect, 2)
    text_surf = my_font2.render(username, True, (0, 0, 0))
    screen.blit(text_surf, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(150, text_surf.get_width() + 10)

    pontos_txt = my_font.render(f'SEUS PONTOS >> {PONTOS_INICIAIS}', False, 'Red')
    pontos_rect = pontos_txt.get_rect(center=(250, 50))
    screen.blit(pontos_txt, pontos_rect)
    screen.blit(jogando, jogando_rect)
    draw.rect(screen, 'Blue', rect_az, border_radius=15)
    draw.rect(screen, 'Red', rect_ver, border_radius=15)
    # draw.rect(screen, 'Green', rect5, border_radius=50, width=6)
    # draw.rect(screen, 'Orange', rect10, border_radius=50, width=6)
    # draw.rect(screen, 'Dark Blue', rect20, border_radius=50, width=6)
    draw.rect(screen, 'Light Blue', rect_allwin, border_radius=30)
    screen.blit(allwin_txt, allwin_txt_rect)
    draw.circle(screen, 'Green', (124, 400), 31, width=6)
    draw.circle(screen, 'Orange', (215, 400), 33.7, width=6)
    draw.circle(screen, 'Dark Blue', (312, 400), 41.5, width=6)
    screen.blit(moeda5_txt, txt_5_rect)
    screen.blit(moeda10_txt, txt_10_rect)
    screen.blit(moeda20_txt, txt_20_rect)
    aposta_txt = my_font.render(f'APOSTA: {aposta}', False, 'Dark Gray')
    aposta_rect = aposta_txt.get_rect(center=(250, 230))
    screen.blit(aposta_txt, aposta_rect)

    display.update()
    clock.tick(FPS)

pygame.quit()