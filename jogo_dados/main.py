from random import choice
import json
from surfaces import *
from sprites import *
from cobrinha import *
from intermed import *


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
once = True

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
game_state = 'USERNAME'

# * LOOP JOGO
running = True
while running:
    for ev in event.get():
        if ev.type ==   QUIT:
            running = False
        if ev.type == KEYDOWN and ev.key == K_ESCAPE:
            running = False
        
        if game_state == 'USERNAME':
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
                    if username in data:
                        print('username já usado')
                    else:
                        game_state = 'SNAKE_GAME'
                        time.wait(500)
                    
        if game_state == 'BACK_BO':
            if ev.type == MOUSEBUTTONDOWN:
                mouse_pos = mouse.get_pos()
                if not clicou:
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
                if ev.type == KEYDOWN:
                    clicou = False
                    Draw = True
                    can_bet = True
                    placed_bet = False
                    aposta = 0
                    # done_username = True
                    has_bet = False
                    Reset_animation()
                    if ev.key == K_RETURN:
                        game_state = 'RANKINGS'

    if game_state == 'USERNAME':
        screen.fill('#f2e7cc')
        insira_username = my_font.render('Insira seu nome de usuário do insper.', False, 'Black')
        insira_username_rect = insira_username.get_rect(center=(TAMANHO2[0] / 2, TAMANHO2[1] / 2 - 200))
        screen.blit(insira_username, insira_username_rect)
        if type_active:
            colorr = color_active
        else:
            colorr = color_passive

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
        display.flip()

    if game_state == 'RANKINGS':
        screen.fill('#f2e7cc')
        if once:
            with open("RANKINGS.json", 'r+') as f:
                data = json.load(f)
            top3 = []
            i = 1
            for _username, _points in data.items():
                top3.append((_username, _points))
                i += 1
                if i > 4:
                    break
            x = [name[0] for name in top3]
            if username not in x:
                user_points = data[username]
                values = list(data.values())
                user_pos = values.index(user_points) + 1
            once = False

        top1 = my_font.render(f'1º  {top3[0][0]}       {top3[0][1]}', True, 'Red')
        top2 = my_font.render(f'2º  {top3[1][0]}       {top3[1][1]}', True, 'Red')
        _top3 = my_font.render(f'3º  {top3[2][0]}       {top3[2][1]}', True, 'Red')

        if username not in x:
            top_user = my_font.render(f'{user_pos}º  {username}       {user_points}', True, 'Red')

        screen.blit(top1, (300, 100))
        screen.blit(top2, (300, 170))
        screen.blit(_top3, (300, 240))
        if username not in x:
            screen.blit(top_user, (300, 400))

        display.flip()

    if game_state == 'SNAKE_GAME':
        
        snake_score = rodar_jogo()
        PONTOS_INICIAIS = snake_score
        decision = tela_intermed()
        if decision == 'bet':
            game_state = 'BACK_BO'
        elif decision == 'exit':
            running = False

    # ''' ---------------------------------------------------------------------------------------

    elif game_state == 'BACK_BO':
        if lost:
            game_state = 'RANKINGS'

        if one_time:
            AcessDatabase()
            one_time = False

        # * fundo
        fundo_verde = Surface((600, 600))
        fundo_verde.fill((65,152,10))
        fundo_verde.set_alpha(90)
        tela.blit(fundo_verde, (0,0))

        # * texto seus pontos
        pontos_txt = my_font.render(f'SEUS PONTOS >> {PONTOS_INICIAIS}', False, 'White')
        pontos_rect = pontos_txt.get_rect(center=(300, 35))
        tela.blit(pontos_txt, pontos_rect)

        # * quadrados cores
        if clicou:
            temp_surf = Surface(TAMANHO2, SRCALPHA)
            draw.rect(temp_surf, (0, 0, 255, 20), rect_az, border_radius=15)
            tela.blit(temp_surf, (0,0))
            draw.rect(temp_surf, (255, 0, 0, 50), rect_ver, border_radius=15)
            tela.blit(temp_surf, (0,0))
            if cor == 'vermelho':
                draw.rect(tela, 'Red', rect_ver, border_radius=15, width=3)
            else:
                draw.rect(tela, 'Blue', rect_az, border_radius=15, width=3)
        else:
            draw.rect(tela, 'Blue', rect_az, border_radius=15)
            draw.rect(tela, 'Red', rect_ver, border_radius=15)

        # * fichas e legendas
        tela.blit(ficha_v_5, ficha5_rect)
        tela.blit(ficha_l_10, ficha10_rect)
        tela.blit(ficha_a_20, ficha20_rect)
        tela.blit(ficha_allwin, fichaallwin_rect)
        tela.blit(lg_5, (ficha5_rect.x + 35, ficha5_rect.y + 75))
        tela.blit(lg_10, (ficha10_rect.x + 36, ficha10_rect.y + 95))
        tela.blit(lg_20, (ficha20_rect.x + 50, ficha20_rect.y + 110))
        tela.blit(lg_allwin, (fichaallwin_rect.x + 38, fichaallwin_rect.y + 135))

        # * texto aposta
        aposta_txt = my_font.render(f'APOSTA: {aposta}', False, 'White')
        aposta_rect = aposta_txt.get_rect(center=(300, 230))
        tela.blit(aposta_txt, aposta_rect)

        # * SPRITE DADOS
        if clicou and can_bet:
            Decrease_vel()
        dado_az_group.draw(tela)
        dado_ver_group.draw(tela)
        if not dado_stopped():
            dado_az_group.update()
            dado_ver_group.update()

        # clicou = True
        # cor = 'azul'
        # aposta = 10
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
                        tela.blit(victory, vic_rect)
                        surf.fill('Red')
                        surf.set_alpha(90)
                        tela.blit(surf, (0,0))
                        win = True
                    elif WinningSide == 'azul':
                        tela.blit(defeat, def_rect)
                        surf.fill('#5657FF')
                        surf.set_alpha(90)
                        tela.blit(surf, (0,0))
                        win = False
                    else:
                        tela.blit(tie, tie_rect)
                        win = 'tie'
                elif cor == 'azul':
                    if WinningSide == 'vermelho':
                        tela.blit(defeat, def_rect)
                        surf.fill('Red')
                        surf.set_alpha(90)
                        tela.blit(surf, (0,0))
                        win = False
                    elif WinningSide == 'azul':
                        tela.blit(victory, vic_rect)
                        surf.fill('#5657FF')
                        surf.set_alpha(90)
                        tela.blit(surf, (0,0))
                        win = True
                    else:
                        tela.blit(tie, tie_rect)
                        win = 'tie'
                if can_bet:
                    betting(aposta, win)
                    can_bet = False

                if PONTOS_INICIAIS == 0:
                    lost = True

                tela.blit(play_again, again_rect)
                tela.blit(play_again2, again2_rect)

        display.flip()
        clock.tick(FPS)

pygame.quit()
''' END
'''