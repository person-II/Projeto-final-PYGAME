from pygame import *
import pygame

# * CLASSES SPRITES
class DadoAzul(pygame.sprite.Sprite):
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
        self.rect = self.image.get_rect(topleft=(355, y_pos))
        self.vel = 0.12
    
    def animation_red(self):
        self.index += self.vel
        if self.index >= len(self.frames):
            self.index = 0
        self.image = self.frames[int(self.index)]

    def update(self):
        self.animation_red()

# * GRUPOS SPRITE
dado_az_group = sprite.Group()
dado_az_group.add(DadoAzul(y_pos=60))
dado_az_group.add(DadoAzul(y_pos=130))
dado_ver_group = sprite.Group()
dado_ver_group.add(DadoVermelho(y_pos=60))
dado_ver_group.add(DadoVermelho(y_pos=130))
