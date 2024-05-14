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