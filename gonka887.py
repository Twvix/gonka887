 # # import sys
 # # from os import mkdir,rmdir
 # # mkdir('./system32')
 # # rmdir('./system32')
 # # sys.exit(0)
# import
from pygame import *
from random import *
#globlal
global bgvgv
global s
bgvgv = 0
s = 0
#variables
game = True
a = int(input('Плотность траффика в полосе от 1 до 5:'))
b = int(input('Скорость траффика(1 - медленнее, 2 - быстрее, 3 - очень быстро):'))
l = 0
#sprite groups
monsters = sprite.Group()
player = sprite.Group()
monst = sprite.Group()
group = sprite.Group()
group1 = sprite.Group()
#display settings
clock = time.Clock()
window = display.set_mode((1600, 900))
display.set_caption('RUN')
background = transform.scale(image.load('doroga.jpg'), (1600, 900))
#classes
#mother class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_w, player_h, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#player
class Player(GameSprite):
    def update(self):
        global key_pressed
        #upravlenie
        key_pressed = key.get_pressed()
        if key_pressed[K_a]:
            self.rect.x -= self.speed
        if key_pressed[K_d]:
              self.rect.x += self.speed
        if key_pressed[K_w]:
            self.rect.y -= self.speed
        if key_pressed[K_s]:
            self.rect.y += self.speed
#traffic
class Enemy(GameSprite):
      direction = 'dawn'
      def update(self):
          if self.direction == 'dawn':
              self.rect.y += self.speed
          if self.rect.y >= 900:
              self.rect.y = randint(-100, -50)
              self.rect.x = randint(250, 700)
              self.speed = b
for i in range(a):
      monster = Enemy('mashi_(1)-transformed.png', 125, 200,randint(300, 700), randint(-1000, -400), b)
      monster.add(monsters)
class Enem(GameSprite):
    directio = 'up'
    def update(self):
            if self.directio == 'up':
                self.rect.y -= self.speed
            if self.rect.y <= -200:
                self.rect.y = randint(300, 900)
                self.rect.x = randint(750, 1200)
                self.speed = b

class Ene(GameSprite):
    directio = 'up'
    def update(self):
            if self.directio == 'up':
                self.rect.y -= self.speed
            if self.rect.y <= -200:
                self.rect.y = randint(300, 900)
                self.rect.x = 770
                self.speed = b
class En(GameSprite):
    directi = 'dawn'
    def update(self):
            if self.directi == 'dawn':
                self.rect.y += self.speed
            if self.rect.y <= -200:
                self.rect.y = randint(-100, -50)
                self.rect.x = 650
                self.speed = b
""""""""
#add objects
for i in range(a):
    monste = Enem('mashina (1).png', 125, 250,randint(750, 1100), randint(300, 900), b)
    monst.add(monste)
hero = Player('lb (1).png', 125, 250,1400,100,4)
#music
mixer.init()
mixer.music.load('bmw-zvuk-motora-s-turbinami-v8.mp3')
mixer.music.play(loops=1000000)
#text
font.init()
font2 = font.Font(None, 36)
#main loop
fi = False
while game:
    if not fi:
        #blit, update, draw, reset
        window.blit(background, (0, 0))
        hero.reset()
        hero.update()
        tex3 = font2.render('Ты проиграл', 1, (0, 0, 0))
        monst.update()
        monst.draw(window)
        monsters.update()
        monsters.draw(window)
        group.update()
        group.draw(window)
        group1.update()
        group1.draw(window)
        ###################
        bgvgv += 1
        #time
        if bgvgv == 60:
            s += 1
            bgvgv = 0
        #collides
        if sprite.spritecollide(hero, monsters, False):
            fi = True
        if sprite.spritecollide(hero, monst, False):
            fi = True
            window.blit(tex3, (1000, 600))
        #EXIT
        if key_pressed[K_ESCAPE]:
            game = False
        
        if s == 20 and l == 0:
            background = transform.scale(image.load('dorogaa.jpg'), (1600, 900))
            for i in range(a):
                mons = Ene('mashina (1).png', 125, 200,770, randint(300, 900), b)
                group.add(mons)
            for monste in monst:
                monste.kill()
            mos = En('mashi_(1)-transformed.png', 125, 200,650, randint(-100, -50), b)
            group1.add(mos)
            for monster in monsters:
                monster.kill()
            s = 0
            l += 1
        if s == 40 and l == 1:
            background = transform.scale(image.load('dorogaaa.jpg'), (1600, 900))
            for i in range(a):
                monste = Enem('mashina (1).png', 125, 250,randint(750, 1100), randint(300, 900), b)
                monst.add(monste)
            for i in range(a):
                monster = Enemy('mashi_(1)-transformed.png', 125, 200,randint(300, 700), randint(-1000, -400), b)
                monster.add(monsters)

    #QUIT
    for e in event.get():
        if e.type == QUIT:
            game = False 
    #display update              
    display.update()
    clock.tick(60)
