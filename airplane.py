import pygame as pg, time, math, sys
from pygame.locals import *
from random import randint

class Airplane:

    def __init__(self, screen):
        self.x = 660
        self.y = randint(1,3)*20
        self.sprite = pg.image.load("images/airplane.png")
        self.sprite = pg.transform.scale(self.sprite,(150,42))
        self.screen = screen
    def draw(self):
        #showing the image
        self.screen.blit(self.sprite, (self.x,self.y))
        self.mask = pg.mask.from_surface(self.sprite)#(center=(self.x + 105,self.y + 29.5))
    def move(self,speed):
        self.x -= speed;
    def on_screen(self):
        if (self.x + 210) > 0: # + 150
            return True
        return False
