import pygame as py
import random


py.init()
py.display.set_caption("ACADEMIA PYTHON COBRINHA")
largura, altura = 1300, 700
tela = py.display.set_mode((largura, altura))
telafim = py.display.set_mode((largura, altura))
relogio = py.time.Clock()

#foto fundo
fundo = py.image.load('assets/acad.png').convert_alpha()
fundo.set_alpha(190)
fundo = py.transform.scale(fundo, (largura, altura))

# cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# parametros da cobrinha
tamanho_quadrado_cobra = 50
tamanho_quadrado_comida = 50
velocidade_jogo = 5

#foto corpo
fotocobra = py.image.load('assets/prof.png').convert_alpha()
fotocobra = py.transform.scale(fotocobra, (tamanho_quadrado_cobra, tamanho_quadrado_cobra))
profinteiro = py.transform.scale(fotocobra, (largura,altura))

#foto prof fim
proffim = py.image.load('assets/proffim.jpeg')
proffim = py.transform.scale(proffim, (largura,altura))

#foto comida
fotocomida = py.image.load('assets/bitcoin.png').convert_alpha()
fotocomida = py.transform.scale(fotocomida, (tamanho_quadrado_comida, tamanho_quadrado_comida))

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado_comida) / float(tamanho_quadrado_comida)) * float(tamanho_quadrado_comida)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado_comida) / float(tamanho_quadrado_comida)) * float(tamanho_quadrado_comida)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    tela.blit(fotocomida, [comida_x,comida_y])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        tela.blit(fotocobra, (pixel[0], pixel[1]))

def desenhar_pontuacao(pontuacao):
    fonte = py.font.SysFont("Verdana", 35)
    texto = fonte.render(f"Pontos: {pontuacao*10}", True, vermelha)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla, velocidade_x, velocidade_y):
    if (tecla == py.K_s or tecla == py.K_DOWN) and velocidade_y != -tamanho_quadrado_cobra:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado_cobra
    
    elif (tecla == py.K_w or tecla == py.K_UP) and velocidade_y != tamanho_quadrado_cobra:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado_cobra

    elif (tecla == py.K_d or tecla == py.K_RIGHT) and velocidade_x != -tamanho_quadrado_cobra:
        velocidade_x = tamanho_quadrado_cobra
        velocidade_y = 0

    elif (tecla == py.K_a or tecla == py.K_LEFT)  and velocidade_x != tamanho_quadrado_cobra:
        velocidade_x = -tamanho_quadrado_cobra
        velocidade_y = 0

    return velocidade_x, velocidade_y

def guarda_pontuacao(pontuacao):
    pont = pontuacao*10
    return pont

def desenhar_grid():
    
    cor_clara = (50, 50, 50)  # Cor mais clara para o grid
    cor_escura = (30, 30, 30)  # Cor mais escura para o grid
    for i in range(0, largura, tamanho_quadrado_cobra):
        for j in range(0, altura, tamanho_quadrado_cobra):
            if (i // tamanho_quadrado_cobra) % 2 == 0:
                if (j // tamanho_quadrado_cobra) % 2 == 0:
                    cor = cor_clara
                else:
                    cor = cor_escura
            else:
                if (j // tamanho_quadrado_cobra) % 2 == 0:
                    cor = cor_escura
                else:
                    cor = cor_clara
            py.draw.rect(tela, cor, py.Rect(i, j, tamanho_quadrado_cobra, tamanho_quadrado_cobra))

def tela_fim(pontuacao):
    tela.fill(preta)
    fonte = py.font.SysFont("Impact", 40)
    texto = fonte.render(f"VOCÊ GANHOU: ", True, vermelha)
    pont = fonte.render(f"{pontuacao*10} PONTOS", True, verde)
    tela.blit(proffim, [0,0])
    tela.blit(texto, [(largura // 2 - texto.get_width() // 2)-80, (altura // 2 - texto.get_height() // 2)-120])
    tela.blit(pont,[(largura/2)-150, (altura/2)-100])
    
    py.display.update()
    py.time.wait(4000)

#código do jogo em si

def rodar_jogo():
    py.display.set_mode((1300, 700))
    veloc = velocidade_jogo
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)
        desenhar_grid()
        tela.blit(fundo, (0,0))
        
        for event in py.event.get():
            # if event.type == py.QUIT:
            #     fim_jogo = True
            if event.type == py.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(event.key, velocidade_x, velocidade_y)

        # desenhar_comida
        desenhar_comida(tamanho_quadrado_comida, comida_x, comida_y)

        # atualizar a posicao da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        # desenhar_cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # se a cobrinha bateu no proprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
                
        desenhar_cobra(tamanho_quadrado_cobra, pixels)

        # desenhar_pontos
        desenhar_pontuacao(tamanho_cobra - 1)

        # atualizacao da tela
        py.display.update()

        #nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            veloc += 0.5 
            comida_x, comida_y = gerar_comida()

        relogio.tick(veloc)
        #pegar pontuacao final:
        # guarda_pontuacao(tamanho_cobra-1)

        if fim_jogo:
            tela_fim(tamanho_cobra - 1)
            # decision = tela_intermed()
            # if decision == 'bet':
            #     pass
            #     # Transition to back bo game
            # elif decision == 'exit':
            #     pass
            #     # Exit the game or return to main menu
            return guarda_pontuacao(tamanho_cobra - 1)

# rodar_jogo()