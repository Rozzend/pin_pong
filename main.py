from pygame import *
from random import randint

font.init()
font = font.Font(None, 35)
lose1 = font.render("PLAYER 1 YOU LOSE", True, (255, 255, 255))
lose2 = font.render('PLAYER 2 YOU LOSE', True, (255, 255, 255))

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
       ball.rect.x += speed_x
       ball.rect.y += speed_y

       if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
           speed_x *= -1
           speed_y *= 1

       if ball.rect.y > win_height-50 or ball.rect.y < 0:
           speed_y *= -1

       if ball.rect.x < 0:
           finish = True
           window.blit(lose1, (200, 200))
           game_over = True

       if ball.rect.x > win_width:
           finish = True
           window.blit(lose2, (200, 200))
           game_over = True

       racket1.reset()
       racket2.reset()
       ball.reset()

   display.update()
   clock.tick(FPS)
