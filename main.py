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
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 160:
           self.rect.y += self.speed
    def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 160:
           self.rect.y += self.speed


win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("pin_pong")
background = transform.scale(image.load("blue.png"), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 100

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3

while game:
   #событие нажатия на кнопку Закрыть
   for e in event.get():
       if e.type == QUIT:
           game = False

 #сама игра: действия спрайтов, проверка правил игры, перерисовка
   if not finish:
       #обновляем фон
       window.blit(background,(0,0))
       racket1.update_l()
       racket2.update_r()

       racket1.reset()
       racket2.reset()
       ball.reset()

   display.update()
   clock.tick(FPS)
