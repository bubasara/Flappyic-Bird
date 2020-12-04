import pygame as pg, time, math, sys
from pygame.locals import *
from random import randint

class Coin:

    def __init__(self, screen):
        self.x = 660
        self.y = randint(0,19)*20
        self.sprite = pg.image.load("images/coin.png")
        self.sprite = pg.transform.scale(self.sprite,(20,20))
        self.screen = screen
    def draw(self):
        #showing the image
        self.screen.blit(self.sprite, (self.x,self.y))
        self.mask = pg.mask.from_surface(self.sprite)
    def move(self,speed):
        self.x -= speed;
    def on_screen(self):
        if (self.x + 20) > 0:
            return True
        return False
