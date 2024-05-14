import pygame
import random


pygame.init()
pygame.display.set_caption("ACADEMIA PYTHON COBRINHA")
largura, altura = 1300, 700
tela = pygame.display.set_mode((largura, altura))
telafim = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#foto fundo
fundo = pygame.image.load('acad.png').convert_alpha()
fundo.set_alpha(190)
fundo = pygame.transform.scale(fundo, (largura, altura))

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
fotocobra = pygame.image.load('prof.png')
fotocobra = pygame.transform.scale(fotocobra, (tamanho_quadrado_cobra, tamanho_quadrado_cobra))
profinteiro = pygame.transform.scale(fotocobra, (largura,altura))
#foto comida
fotocomida = pygame.image.load('bitcoin.png').convert_alpha()
fotocomida = pygame.transform.scale(fotocomida, (tamanho_quadrado_comida, tamanho_quadrado_comida))

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
    fonte = pygame.font.SysFont("Verdana", 35)
    texto = fonte.render(f"Pontos: {pontuacao}x", True, vermelha)
    tela.blit(texto, [1, 1])
