global key_pressed
from pygame import *
from random import *

clock = time.Clock()
window = display.set_mode((1600, 900))
display.set_caption('RUN')
background = transform.scale(image.load('rofl.jpg'), (1600, 900))
b = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_w, player_h, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
monster = GameSprite('pistol-.png', 300, 200,800, 460)


font.init()
font2 = font.Font(None, 52)
key_pressed = key.get_pressed()

game = True
fi = False
while game:
    if not fi:
        tex3 = font2.render('Ты проиграл', 1, (255, 255, 255))
        window.blit(background, (0, 0))
        monster.reset()
        monster.update()
        if key_pressed[K_ESCAPE]:
            game = False
            #QUIT
    for e in event.get():
        if e.type == QUIT:
            game = False 
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                a = randint(1, 6)
                b += 1
                if a == 1:
                    window.blit(tex3, (1000, 600))
                    background = transform.scale(image.load('rofl-.jpg'), (1600, 900))
                    # fi = True
                    print('Ты проиграл с(о) ', b, ' попытки')
    #display update              
    display.update()
    clock.tick(60)
