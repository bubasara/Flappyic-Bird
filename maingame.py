import pygame, time, math, sys
from pygame.locals import *
from random import randint
from bird import Bird
from enemy_bird import EnemyBird
from airplane import Airplane
from building import Building
from coin import Coin
from copy import copy

#constants
W, H = 640, 400
FPS = 60
GEN_EVENT,GEN_OBJ_PERIOD = pygame.USEREVENT+1, 6000
GEN_EVENT_COIN, GEN_COIN_OBJ_PERIOD = pygame.USEREVENT+2, 9000 
GEN_EVENT_BUILD, GEN_BUILD_OBJ_PERIOD = pygame.USEREVENT+3, 4000

bg_x = 0
points = 0

background = pygame.transform.scale(pygame.image.load("images/background.png"),(W,H))
game_over_sprite = pygame.transform.scale(pygame.image.load("images/game-over.png"),(250,175))

pygame.mixer.pre_init(44100, 16, 2, 2048)
pygame.init()
coin_sound = pygame.mixer.Sound('sounds/coin.wav')

clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))

bird = Bird(screen,H);
enemy_bird_prototype = EnemyBird(screen,H)

active_objects = []
coin_objects = []

pygame.time.set_timer(GEN_EVENT, GEN_OBJ_PERIOD)
pygame.time.set_timer(GEN_EVENT_COIN, GEN_COIN_OBJ_PERIOD)
pygame.time.set_timer(GEN_EVENT_BUILD, GEN_BUILD_OBJ_PERIOD)

execute_game = True

def generate_random_object(screen):
    rand_int = randint(0,1);
    if(rand_int == 0):
        enemy_bird = copy(enemy_bird_prototype)
        enemy_bird.copy_setter(H)
        return enemy_bird;
    return Airplane(screen);

def generate_random_building(screen):
    return Building(screen);

def generate_coin_object(screen):
    return Coin(screen)

#convert string to displayable object
def string_to_object(text, font):
    text_surface = font.render(text, True, (255,0,0)) #(255,255,255)) #(241,210,0))
    return text_surface, text_surface.get_rect()

def string_display(text):
    text_font = pygame.font.Font('fonts/LATINWD.ttf', 18)
    text_surface, text_rect = string_to_object(text, text_font)
    screen.blit(text_surface, (250, 330))
    pygame.display.update()

#game over
def game_over():
    screen.blit(game_over_sprite, (195, 137))
    string_display("points: " + str(int(points)))

    
pygame.mixer.music.load('sounds/background-music.mp3')
pygame.mixer.music.play(-1)

game_time = 0;
obj_speed = 1;

while execute_game:
    clock.tick(FPS)
    points += 0.5
    #listen for events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                execute_game = False
        if event.type == GEN_EVENT:
            active_objects.append(generate_random_object(screen))
        if event.type == GEN_EVENT_COIN:
            coin_objects.append(generate_coin_object(screen))
        if event.type == GEN_EVENT_BUILD:
            active_objects.append(generate_random_building(screen))

    #get pressed keys
    pressed_keys = pygame.key.get_pressed()

    #move objects
    bird.move(pressed_keys)
    for obj in active_objects:
        obj.move(obj_speed)

    for obj in coin_objects:
        obj.move(obj_speed + 1)

    #update screen
    screen.blit(background, (bg_x,0))

    #draw objects
    bird.draw()
    for obj in active_objects:
        obj.draw()

    for obj in coin_objects:
        obj.draw()

    pygame.display.update()

    #remove objects that aren't on screen
    active_objects = [obj for obj in active_objects if obj.on_screen()]

    if bird.is_collided(active_objects):
        execute_game = False
    game_time += 1
    if(game_time % 1000 == 0):
        obj_speed += 1;
        pygame.time.set_timer(GEN_EVENT, GEN_OBJ_PERIOD//obj_speed)
        pygame.time.set_timer(GEN_EVENT_BUILD, GEN_BUILD_OBJ_PERIOD // obj_speed)
    if bird.is_collided(coin_objects):
        coin_objects = []
        coin_sound.play()
        points += 200

#when game is over
game_over()
pygame.display.update()
time.sleep(5)
pygame.quit()
