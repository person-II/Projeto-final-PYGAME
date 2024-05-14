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


