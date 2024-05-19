from pygame import *

init()

# * CONSTANTES
# VALORES
TAMANHO = (530, 600)
FPS = 60

# JANELA E CLOCK
screen = display.set_mode(TAMANHO)
clock = time.Clock()
display.set_caption('dado')

# FONTES
my_font = font.Font('assets/fontt/open-sans/OpenSans-Regular.ttf', 30)
my_font2 = font.Font('assets/fontt/open-sans/OpenSans-Regular.ttf', 25)
my_font3 = font.Font('assets/fontt/open-sans/OpenSans-Regular.ttf', 15)
