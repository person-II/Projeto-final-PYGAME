from random import choice
import json
from surfaces import *
from sprites import *


''' -----------------------------------------------------------------------------------------------
'''

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

''' --------------------------------------------------------------------------------------
'''

# * FUNÇÕES
def jogar_dados2():
    for ob, ob2 in zip(dado_az_group, dado_ver_group):
        ob.image = choice(ob.frames)
        ob2.image = choice(ob2.frames)

def FaceValue(group):
    values = []
    for ob in group:
        if ob.image == ob.frames[0]:
            value = 1
        if ob.image == ob.frames[1]:
            value = 2
        if ob.image == ob.frames[2]:
            value = 3
        if ob.image == ob.frames[3]:
            value = 4
        if ob.image == ob.frames[4]:
            value = 5
        if ob.image == ob.frames[5]:
            value = 6
        values.append(value)

    return values[0], values[1]

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
        if ob.vel <= 0.05:
            return True
    return False

def winning_side(value1_az, value2_az, value1_ver, value2_ver):
    sum_az = value1_az + value2_az
    sum_ver = value1_ver + value2_ver

    if sum_az > sum_ver:
        return 'azul'
    elif sum_az < sum_ver:
        return  'vermelho'
    else:
        return 'tie'

''' -------------------------------------------------------------------------------------------
'''

surf = Surface((530, 600))



# * LOOP JOGO
running = True
while running:

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        elif ev.type == KEYDOWN and ev.key == K_ESCAPE:
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
                    cor = 'azul'

                elif rect_ver.collidepoint(mouse_pos):
                    clicou = True
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
    
    fundo_verde = Surface((530, 600))
    fundo_verde.fill((65,152,10))
    fundo_verde.set_alpha(90)
    screen.blit(fundo_verde, (0,0))
    
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
    pontos_txt = my_font.render(f'SEUS PONTOS >> {PONTOS_INICIAIS}', False, 'White')
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
    screen.blit(lg_allwin, (fichaallwin_rect.x + 38, fichaallwin_rect.y + 135))

    # * texto aposta
    aposta_txt = my_font.render(f'APOSTA: {aposta}', False, 'White')
    aposta_rect = aposta_txt.get_rect(center=(265, 230))
    screen.blit(aposta_txt, aposta_rect)

    # * SPRITE DADOS
    if clicou and can_bet:
        Decrease_vel()
    dado_az_group.draw(screen)
    dado_ver_group.draw(screen)
    if not dado_stopped():
        dado_az_group.update()
        dado_ver_group.update()

    # * JOGO / APOSTA
    if clicou:
        if dado_stopped():
            if Draw:
                jogar_dados2()
                time.wait(400)
                
                value1_az, value2_az = FaceValue(dado_az_group)
                value1_ver, value2_ver = FaceValue(dado_ver_group)
                print('--------------------------')
                print('LADO = ', cor)
                print('value 1 azul =', value1_az)
                print('value 2 azul =', value2_az)
                print('soma azul =', value1_az + value2_az)
                print('value 1 vermelho =', value1_ver)
                print('value 2 vermelho =', value2_ver)
                print('soma vermelho =', value1_ver + value2_ver)

                Draw = False
        
            WinningSide = winning_side(value1_az, value2_az, value1_ver, value2_ver)
            if cor == 'vermelho':
                if WinningSide == 'vermelho':
                    screen.blit(victory, vic_rect)
                    surf.fill('Red')
                    surf.set_alpha(90)
                    screen.blit(surf, (0,0))
                    win = True
                elif WinningSide == 'azul':
                    screen.blit(defeat, def_rect)
                    surf.fill('#5657FF')
                    surf.set_alpha(90)
                    screen.blit(surf, (0,0))
                    win = False
                else:
                    screen.blit(tie, tie_rect)
                    win = 'tie'
            elif cor == 'azul':
                if WinningSide == 'vermelho':
                    screen.blit(defeat, def_rect)
                    surf.fill('Red')
                    surf.set_alpha(90)
                    screen.blit(surf, (0,0))
                    win = False
                elif WinningSide == 'azul':
                    screen.blit(victory, vic_rect)
                    surf.fill('#5657FF')
                    surf.set_alpha(90)
                    screen.blit(surf, (0,0))
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
''' END
'''