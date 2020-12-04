import pygame as pg
from random import randint

class EnemyBird():
    def __init__(self, screen,y):
        self.x = 660
        self.y = y/2
        self.sprite = [
            pg.transform.scale(pg.image.load("images/enemy-bird/enemy-frame-1.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/enemy-bird/enemy-frame-2.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/enemy-bird/enemy-frame-3.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/enemy-bird/enemy-frame-4.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/enemy-bird/enemy-frame-5.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/enemy-bird/enemy-frame-6.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/enemy-bird/enemy-frame-7.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/enemy-bird/enemy-frame-8.png"),(65,50))
        ]
        self.screen = screen
        self.current_sprite = 0

    def draw(self):
        self.screen.blit(self.sprite[self.current_sprite // 4],(self.x,self.y))
        self.update_current_sprite()

    def move(self, speed):
        self.x -= speed + 1
        rand_y = randint(-5,5)
        self.y += rand_y

    def update_current_sprite(self):
        if (self.current_sprite < 31):
            self.current_sprite += 1;
        else:
            self.current_sprite = 0;
        self.mask = pg.mask.from_surface(self.sprite[self.current_sprite // 4])#.get_rect(center=(self.x + 32.5,self.y + 25))

    def copy_setter(self,y):
        self.x = 660
        self.y = y/2
        
    def on_screen(self):
        if (self.x + 65) > 0:
            return True
        return False
