from constantes import *

# * IMAGENS / SURFACES ..

# ? mendagem derrota vitoria
victory = my_font.render('VITORIA', False, 'Black')
defeat = my_font.render('DERROTA', False, 'Black')
tie = my_font.render('EMPATE', False, 'Black')
vic_rect = victory.get_rect(center=(265, 150))
def_rect = defeat.get_rect(center=(265, 150))
tie_rect = tie.get_rect(center=(265, 150))

# ? quadrado escolha cor
rect_ver_surf = Surface((100, 65))
rect_az_surf = Surface((100, 65))
rect_ver = rect_ver_surf.get_rect(topleft=(275, 270))
rect_az = rect_az_surf.get_rect(topleft=(125, 270))

# ? espaço para play again
play_again = my_font2.render('pressione espaço para', False, 'Black')
play_again2 = my_font2.render('jogar novamente', False, 'Black')
again_rect = play_again.get_rect(center=(265, 480))
again2_rect = play_again2.get_rect(center=(265, 505))

# ? fichas e legendas
ficha_v_5 = image.load('assets/jogo dados/ficha vermelha.png')
ficha_l_10 = image.load('assets/jogo dados/ficha laranja.png')
ficha_a_20 = image.load('assets/jogo dados/ficha azul.png')
ficha_allwin = image.load('assets/jogo dados/ficha all win.png')
ficha_v_5 = transform.scale(ficha_v_5, (85, 85))
ficha_l_10 = transform.scale(ficha_l_10, (105, 105))
ficha_a_20 = transform.scale(ficha_a_20, (125, 125))
ficha_allwin = transform.scale(ficha_allwin, (145, 145))
ficha5_rect = ficha_v_5.get_rect(midleft=(40, 400))
ficha10_rect = ficha_v_5.get_rect(midleft=(125, 390))
ficha20_rect = ficha_v_5.get_rect(midleft=(220, 380))
fichaallwin_rect = ficha_allwin.get_rect(midleft=(330, 400))
lg_5 = my_font2.render('5', False, 'Black')
lg_10 = my_font2.render('10', False, 'Black')
lg_20 = my_font2.render('20', False, 'Black')
lg_allwin = my_font2.render('ALL IN', False, 'Black')

# ? caixa enter texto
enter_button = Surface((100, 55))
enter_button_rect = enter_button.get_rect(topleft=(10, 540))
enter_txt = my_font2.render('Enter', False, 'Black')
enter_txt_rect = enter_txt.get_rect(topleft=(28, 550))

# ? caixa de texto
username = ''
input_rect = Rect(120, 540, 140, 55)
color_active = Color('Light Gray')
color_passive = Color('lightskyblue3')
colorr = color_passive
type_active = False