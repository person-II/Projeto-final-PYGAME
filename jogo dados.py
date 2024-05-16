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

ficha_v_5 = image.load('assets/ficha vermelha.png')
ficha_l_10 = image.load('assets/ficha laranja.png')
ficha_a_20 = image.load('assets/ficha azul.png')
ficha_allwin = image.load('assets/ficha all win.png')
ficha_v_5 = transform.scale(ficha_v_5, (85, 85))
ficha_l_10 = transform.scale(ficha_l_10, (105, 105))
ficha_a_20 = transform.scale(ficha_a_20, (125, 125))
ficha_allwin = transform.scale(ficha_allwin, (145, 145))
ficha5_rect = ficha_v_5.get_rect(midleft=(40, 400))
ficha10_rect = ficha_v_5.get_rect(midleft=(125, 390))
ficha20_rect = ficha_v_5.get_rect(midleft=(220, 380))
fichaallwin_rect = ficha_allwin.get_rect(midleft=(330, 400))
lg_5 = my_font2.render('5')
lg_10 = my_font2.render('10')
lg_20 = my_font2.render('20')
lg_allwin = my_font2.render('ALL WIN')

enter_button = Surface((100, 55))
enter_button_rect = enter_button.get_rect(topleft=(10, 540))
enter_txt = my_font2.render('Enter', False, 'Black')
enter_txt_rect = enter_txt.get_rect(topleft=(28, 550))

# * USERNAME
username = ''
input_rect = Rect(120, 540, 140, 55)
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
one_time = True
done_username = False
lost = False


running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
        
        if ev.type == MOUSEBUTTONDOWN:
            if input_rect.collidepoint(ev.pos):
                if not done_username:
                    type_active = True
            else:
                type_active = False

        if ev.type == KEYDOWN:
            if type_active:
                if ev.key == K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += ev.unicode

        if ev.type == MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()
            if enter_button_rect.collidepoint(mouse_pos):
                with open("RANKINGS.json") as f:
                    data = json.load(f)
                if username not in data:
                    done_username = True
                else:
                    if not done_username:
                        print('username já usado')

        if mouse.get_pressed()[0] and not clicou and done_username:
            mouse_pos = mouse.get_pos()
            if ficha5_rect.collidepoint(mouse_pos):
                valor = 5
                if valor <= PONTOS_INICIAIS:
                    aposta += valor
                    PONTOS_INICIAIS -= valor
                    placed_bet = True
            elif ficha10_rect.collidepoint(mouse_pos):
                valor = 10
                if valor <= PONTOS_INICIAIS:
                    aposta += valor
                    PONTOS_INICIAIS -= valor
                    placed_bet = True
            elif ficha20_rect.collidepoint(mouse_pos):
                valor = 20
                if valor <= PONTOS_INICIAIS:
                    aposta += valor
                    PONTOS_INICIAIS -= valor
                    placed_bet = True
            elif fichaallwin_rect.collidepoint(mouse_pos):
                valor = PONTOS_INICIAIS
                if valor <= PONTOS_INICIAIS:
                    aposta += valor
                    PONTOS_INICIAIS -= valor
                    placed_bet = True

            if placed_bet:
                if rect_az.collidepoint(mouse_pos):
                    clicou = True
                    print('\n--------------------------\nTIME AZUL')
                    print('> APOSTA:', aposta)
                    cor = 'azul'

                elif rect_ver.collidepoint(mouse_pos):
                    clicou = True
                    print('\n--------------------------\nTIME VERMELHO')
                    print('> APOSTA:', aposta)
                    cor = 'vermelho'
    
    if type_active:
        colorr = color_active
    else:
        colorr = color_passive
    
    screen.fill((94, 129, 162))
    if done_username:
        color_enter_button = 'Dark Gray'
    else:
        color_enter_button = 'Light Gray'
    draw.rect(screen, color_enter_button, enter_button_rect, border_radius=10)
    screen.blit(enter_txt, enter_txt_rect)
    draw.rect(screen, colorr, input_rect, 2)
    text_surf = my_font2.render(username, True, (0, 0, 0))
    screen.blit(text_surf, (input_rect.x + 5, input_rect.y + 8))
    input_rect.w = max(150, text_surf.get_width() + 10)

    pontos_txt = my_font.render(f'SEUS PONTOS >> {PONTOS_INICIAIS}', False, 'Red')
    pontos_rect = pontos_txt.get_rect(center=(265, 50))
    screen.blit(pontos_txt, pontos_rect)
    screen.blit(jogando, jogando_rect)
    draw.rect(screen, 'Blue', rect_az, border_radius=15)
    draw.rect(screen, 'Red', rect_ver, border_radius=15)

    screen.blit(ficha_v_5, ficha5_rect)
    screen.blit(ficha_l_10, ficha10_rect)
    screen.blit(ficha_a_20, ficha20_rect)
    screen.blit(ficha_allwin, fichaallwin_rect)

    screen.blit(lg_5, (ficha5_rect.x + 35, ficha5_rect.y + 75))
    screen.blit(lg_10, (ficha10_rect.x + 36, ficha10_rect.y + 95))
    screen.blit(lg_20, (ficha20_rect.x + 50, ficha20_rect.y + 110))
    screen.blit(lg_allwin, (fichaallwin_rect.x + 25, fichaallwin_rect.y + 135))

    aposta_txt = my_font.render(f'APOSTA: {aposta}', False, 'Dark Gray')
    aposta_rect = aposta_txt.get_rect(center=(265, 230))
    screen.blit(aposta_txt, aposta_rect)

    display.update()
    clock.tick(FPS)

pygame.quit()