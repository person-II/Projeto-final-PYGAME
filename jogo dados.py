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
my_font = font.SysFont('OpenSans-Regular', 30)
my_font2 = font.SysFont('OpenSans-Regular', 25)
my_font3 = font.SysFont('OpenSans-Regular', 15)

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

ficha_v_5 = image.load('snake game/assets/ficha vermelha.png')
ficha_l_10 = image.load('snake game/assets/ficha laranja.png')
ficha_a_20 = image.load('snake game/assets/ficha azul.png')
ficha_allwin = image.load('snake game/assets/ficha all win.png')
ficha_v_5 = transform.scale(ficha_v_5, (85, 85))
ficha_l_10 = transform.scale(ficha_l_10, (105, 105))
ficha_a_20 = transform.scale(ficha_a_20, (125, 125))
ficha_allwin = transform.scale(ficha_allwin, (145, 145))
ficha5_rect = ficha_v_5.get_rect(midleft=(40, 400))
ficha10_rect = ficha_v_5.get_rect(midleft=(125, 390))
ficha20_rect = ficha_v_5.get_rect(midleft=(220, 380))
fichaallwin_rect = ficha_allwin.get_rect(midleft=(330, 400))

enter_button = Surface((100, 55))
enter_button_rect = enter_button.get_rect(topleft=(10, 540))
enter_txt = my_font2.render('Enter', False, 'Black')
enter_txt_rect = enter_txt.get_rect(topleft=(28, 550))

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
    aposta_txt = my_font.render(f'APOSTA: {aposta}', False, 'Dark Gray')
    aposta_rect = aposta_txt.get_rect(center=(250, 230))
    screen.blit(aposta_txt, aposta_rect)

    display.update()
    clock.tick(FPS)

pygame.quit()