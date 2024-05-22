from pygame import *

init()
mixer.init()

# * CONSTANTES
# VALORES
TAMANHO = (600, 600)
FPS = 60

# JANELA E CLOCK
screen = display.set_mode(TAMANHO)
clock = time.Clock()
display.set_caption('jogo dado')

# FONTES
my_font = font.Font('assets/fontt/open-sans/OpenSans-Regular.ttf', 30)
my_font2 = font.Font('assets/fontt/open-sans/OpenSans-Regular.ttf', 25)
my_font3 = font.Font('assets/fontt/open-sans/OpenSans-Regular.ttf', 15)

# AUDIO

bg_music = mixer.Sound('assets/music.wav')
bg_music.set_volume(0.1)
bg_music.play(loops= -1)
