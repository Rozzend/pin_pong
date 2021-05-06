from pygame import *
from random import randint

font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render("YOU WIN!", True, (255, 255, 255))
lose = font1.render('YOU LOSE', True, (180, 0, 0))

font2 = font.SysFont('Arial', 36)

score = 0
goal = 99999999
lost = 0
max_lost = 99999
life = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("pin_pong")
background = transform.scale(image.load("blue.png"), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 100

while game:
   #событие нажатия на кнопку Закрыть
   for e in event.get():
       if e.type == QUIT:
           game = False
       #событие нажатия на пробел - спрайт стреляет
       elif e.type == KEYDOWN:
           if e.key == K_SPACE:
               fire_sound.play()
               player.fire()
 #сама игра: действия спрайтов, проверка правил игры, перерисовка
   if not finish:
       #обновляем фон
       window.blit(background,(0,0))

       display.update()

   else:
       finish = False
       
   time.delay(25)