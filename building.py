import pygame as pg, time, math, sys
from pygame.locals import *
from random import randint

class Building():
    #initialization
    def __init__(self, screen):
        self.x = 691
        self.y = randint(270, 310)
        self.sprite = pg.image.load("images/building.png")
        self.sprite = pg.transform.scale(self.sprite,(91,130))
        self.screen = screen

    #draw Building object
    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
        self.mask = pg.mask.from_surface(self.sprite)

    #move Building object
    def move(self, speed):
        self.x -= speed;

    #draw while on screen
    def on_screen(self):
        if (self.x + 64) > 0:
            return True
        return False
