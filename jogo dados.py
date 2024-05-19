from pygame import *
import pygame
from random import randint
import json

init()

class DadoAzul(sprite.Sprite):
    def __init__(self, y_pos) -> None:
        super().__init__()

        f1 = image.load('assets/jogo dados/1 az.png').convert_alpha()
        f1 = transform.scale(f1, (80, 80))
        f2 = image.load('assets/jogo dados/2 az.png').convert_alpha()
        f2 = transform.scale(f2, (80, 80))
        f3 = image.load('assets/jogo dados/3 az.png').convert_alpha()
        f3 = transform.scale(f3, (80, 80))
        f4 = image.load('assets/jogo dados/4 az.png').convert_alpha()
        f4 = transform.scale(f4, (80, 80))
        f5 = image.load('assets/jogo dados/5 az.png').convert_alpha()
        f5 = transform.scale(f5, (80, 80))
        f6 = image.load('assets/jogo dados/6 az.png').convert_alpha()
        f6 = transform.scale(f6, (80, 80))

        self.frames = [f1, f2, f3, f4, f5, f6]
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(topleft=(130, y_pos))
        self.vel = 0.12

    def animation_azul(self):
        self.index += self.vel
        if self.index >= len(self.frames):
            self.index = 0
        self.image = self.frames[int(self.index)]
    
    def update(self):
        self.animation_azul()

class DadoVermelho(sprite.Sprite):
    def __init__(self, y_pos) -> None:
        super().__init__()

        f1 = image.load('assets/jogo dados/1 ve.png').convert_alpha()
        f1 = transform.scale(f1, (80, 80))
        f2 = image.load('assets/jogo dados/2 ve.png').convert_alpha()
        f2 = transform.scale(f2, (80, 80))
        f3 = image.load('assets/jogo dados/3 ve.png').convert_alpha()
        f3 = transform.scale(f3, (80, 80))
        f4 = image.load('assets/jogo dados/4 ve.png').convert_alpha()
        f4 = transform.scale(f4, (80, 80))
        f5 = image.load('assets/jogo dados/5 ve.png').convert_alpha()
        f5 = transform.scale(f5, (80, 80))
        f6 = image.load('assets/jogo dados/6 ve.png').convert_alpha()
        f6 = transform.scale(f6, (80, 80))

        self.frames = [f1, f2, f3, f4, f5, f6]
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(topleft=(285, y_pos))
        self.vel = 0.12
    
    def animation_red(self):
        self.index += self.vel
        if self.index >= len(self.frames):
            self.index = 0
        self.image = self.frames[int(self.index)]

    def update(self):
        self.animation_red()

# * CONSTANTES
TAMANHO = (530, 600)
FPS = 60

# * JANELA E CLOCK
screen = display.set_mode(TAMANHO)
clock = time.Clock()
display.set_caption('dado')

# * FONTES
my_font = font.Font('assets/fontt/open-sans/OpenSans-Regular.ttf', 30)
my_font2 = font.Font('assets/fontt/open-sans/OpenSans-Regular.ttf', 25)
my_font3 = font.Font('assets/fontt/open-sans/OpenSans-Regular.ttf', 15)

# * IMAGENS / SURFACES ...
# ? mendagem derrota vitoria
victory = my_font.render('VITORIA', False, 'Black')
defeat = my_font.render('DERROTA', False, 'Black')
tie = my_font.render('EMPATE', False, 'Black')
vic_rect = victory.get_rect(center=(265, 150))
def_rect = defeat.get_rect(center=(265, 150))
tie_rect = tie.get_rect(center=(265, 150))

# ? quadrado escolha cor
rect_ver = Surface((100, 65))
rect_ver.fill('Red')
rect_ver = rect_ver.get_rect(topleft=(275, 270))
rect_az = Surface((100, 65))
rect_az.fill('Blue')
rect_az = rect_az.get_rect(topleft=(125, 270))

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
lg_allwin = my_font2.render('ALL WIN', False, 'Black')

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

# * VARIAVEIS
PONTOS_INICIAIS = 100
clicou = False
can_bet = True
Draw = True
placed_bet = False
aposta = 0
one_time = True
done_username = False
lost = False

# * FUNÇÕES
def jogar_dados():
    return randint(1, 6)

def betting(aposta, win):
    global PONTOS_INICIAIS

    if win == True:
        PONTOS_INICIAIS += (aposta * 2)
    elif win == 'tie':
        PONTOS_INICIAIS += aposta
    elif win == False:    
        pass
        # ja perdeu dinheiro na aposta

def Can_AcessDatabase():
    if one_time:
        if done_username:
            return True
    return False

def AcessDatabase():
    global username
    with open("RANKINGS.json", 'r+') as f:
        data = json.load(f)
        user_count = len(list(data.keys())) + 1
        if not username:
            username = f"user{user_count}"
        data[username] = PONTOS_INICIAIS
        data = dict(sorted(data.items(), key=lambda x:x[1], reverse=True))
        ''' refrencia linha a cima: 
        https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
        '''
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)

def Decrease_vel():
    for ob_az, ob_ver in zip(dado_az_group, dado_ver_group):
        if ob_az.vel > 0:
            ob_az.vel -= 0.0004
            ob_ver.vel -= 0.0004

def Reset_animation():
    for ob_az, ob_ver in zip(dado_az_group, dado_ver_group):
        ob_az.index = 0
        ob_az.vel = 0.12
        ob_ver.index = 0
        ob_ver.vel = 0.12

def dado_stopped():
    for ob in dado_az_group:
        if ob.vel <= 0:
            return True
    return False

# * GRUPOS SPRITE
dado_az_group = sprite.Group()
dado_az_group.add(DadoAzul(y_pos=60))
dado_az_group.add(DadoAzul(y_pos=130))
dado_ver_group = sprite.Group()
dado_ver_group.add(DadoVermelho(y_pos=60))
dado_ver_group.add(DadoVermelho(y_pos=130))

# * LOOP JOGO
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

        if not can_bet:
            one_time = True
            if ev.type == KEYDOWN and ev.key == K_SPACE:
                clicou = False
                Draw = True
                can_bet = True
                placed_bet = False
                aposta = 0
                done_username = True
                has_bet = False
                Reset_animation()

    if lost:
        one_time = True
        done_username = True
      
    if Can_AcessDatabase():
        AcessDatabase()
        one_time = False

    if lost:
        running = False

    if type_active:
        colorr = color_active
    else:
        colorr = color_passive
    
    screen.fill((94, 129, 162))
    if done_username:
        color_enter_button = 'Dark Gray'
    else:
        color_enter_button = 'Light Gray'

    # * enter button
    draw.rect(screen, color_enter_button, enter_button_rect, border_radius=10)
    screen.blit(enter_txt, enter_txt_rect)

    # * caixa de texto
    draw.rect(screen, colorr, input_rect, 2)
    text_surf = my_font2.render(username, True, (0, 0, 0))
    screen.blit(text_surf, (input_rect.x + 5, input_rect.y + 8))
    input_rect.w = max(150, text_surf.get_width() + 10)

    # * texto seus pontos
    pontos_txt = my_font.render(f'SEUS PONTOS >> {PONTOS_INICIAIS}', False, 'Red')
    pontos_rect = pontos_txt.get_rect(center=(265, 35))
    screen.blit(pontos_txt, pontos_rect)

    # * quadrados cores
    draw.rect(screen, 'Blue', rect_az, border_radius=15)
    draw.rect(screen, 'Red', rect_ver, border_radius=15)

    # * fichas e legendas
    screen.blit(ficha_v_5, ficha5_rect)
    screen.blit(ficha_l_10, ficha10_rect)
    screen.blit(ficha_a_20, ficha20_rect)
    screen.blit(ficha_allwin, fichaallwin_rect)
    screen.blit(lg_5, (ficha5_rect.x + 35, ficha5_rect.y + 75))
    screen.blit(lg_10, (ficha10_rect.x + 36, ficha10_rect.y + 95))
    screen.blit(lg_20, (ficha20_rect.x + 50, ficha20_rect.y + 110))
    screen.blit(lg_allwin, (fichaallwin_rect.x + 25, fichaallwin_rect.y + 135))

    # * texto aposta
    aposta_txt = my_font.render(f'APOSTA: {aposta}', False, 'Dark Gray')
    aposta_rect = aposta_txt.get_rect(center=(265, 230))
    screen.blit(aposta_txt, aposta_rect)

    # * SPRITE DADOS
    if clicou:
        Decrease_vel()
    dado_az_group.draw(screen)
    dado_az_group.update()
    dado_ver_group.draw(screen)
    dado_ver_group.update()

    # * JOGO / APOSTA
    if clicou:
        if Draw:
            dado_vermelho = jogar_dados()
            dado_azul = jogar_dados()

            print('> Dado azul:', dado_azul)
            print('> Dado vermelho:', dado_vermelho)
            Draw = False
        
        if dado_stopped():
            time.wait(2000)
            if cor == 'vermelho':
                if dado_vermelho > dado_azul:
                    screen.blit(victory, vic_rect)
                    win = True
                elif dado_vermelho < dado_azul:
                    screen.blit(defeat, def_rect)
                    win = False
                else:
                    screen.blit(tie, tie_rect)
                    win = 'tie'
            elif cor == 'azul':
                if dado_vermelho > dado_azul:
                    screen.blit(defeat, def_rect)
                    win = False
                elif dado_vermelho < dado_azul:
                    screen.blit(victory, vic_rect)
                    win = True
                else:
                    screen.blit(tie, tie_rect)
                    win = 'tie'
            if can_bet:
                betting(aposta, win)
                can_bet = False

            if PONTOS_INICIAIS == 0:
                lost = True

            screen.blit(play_again, again_rect)
            screen.blit(play_again2, again2_rect)

    display.update()
    clock.tick(FPS)

pygame.quit()
