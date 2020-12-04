import pygame as pg


class Bird():
    def __init__(self, screen, y):
        self.x = 10
        self.y = y/2
        self.sprite = [
            pg.transform.scale(pg.image.load("images/bird/frame-1.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/bird/frame-2.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/bird/frame-3.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/bird/frame-4.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/bird/frame-5.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/bird/frame-6.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/bird/frame-7.png"),(65,50)),
            pg.transform.scale(pg.image.load("images/bird/frame-8.png"),(65,50))
        ]
        self.screen = screen
        self.current_sprite = 0
        self.mask = pg.mask.from_surface(self.sprite[self.current_sprite // 4])
        self.flap_sound = pg.mixer.Sound('sounds/wings.wav');
        self.drop_sound = pg.mixer.Sound('sounds/drop.wav');

    def draw(self):
        self.screen.blit(self.sprite[self.current_sprite // 4],(self.x,self.y))
        self.update_current_sprite()
        
    def move(self,pressed_keys):
        if pressed_keys[pg.K_RIGHT] and self.x < 580:
            self.x += 3
        if pressed_keys[pg.K_LEFT] and self.x > 5:
            self.x -= 3
        if pressed_keys[pg.K_UP] and self.y > 5:
            self.y -= 3
        if pressed_keys[pg.K_DOWN] and self.y < 347:
            self.y += 3
        if pressed_keys[pg.K_SPACE] and self.y < 340 and self.x < 570:
            self.y += 5
            self.x += 5
            self.drop_sound.play()
        
    def update_current_sprite(self):
        if (self.current_sprite < 31):
            self.current_sprite += 1;
        else:
            self.current_sprite = 0;
            self.flap_sound.play()

    def is_collided(self,list_of_objects):
        for obj in list_of_objects:
            if(self.mask.overlap(obj.mask,[abs(int(self.x - obj.x)),abs(int(self.y - obj.y))])):
                return True
        return False
