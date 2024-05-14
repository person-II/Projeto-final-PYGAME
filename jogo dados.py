from pygame import *
import pygame
from random import randint
import json

init()

# * CONSTANTES
TAMANHO = (500, 600)
FPS = 60

# * VARIAVEIS
PONTOS_INICIAIS = 100

# * JANELA E CLOCK
screen = display.set_mode(TAMANHO)
clock = time.Clock()
display.set_caption('dado')

# * FONTES
my_font = font.Font('snail game/fontt/open-sans/OpenSans-Regular.ttf', 30)
my_font2 = font.Font('snail game/fontt/open-sans/OpenSans-Regular.ttf', 25)
my_font3 = font.Font('snail game/fontt/open-sans/OpenSans-Regular.ttf', 15)

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

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    display.update()
    clock.tick(FPS)

pygame.quit()