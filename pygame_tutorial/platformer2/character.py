import os
from pygame.sprite import Sprite
from config import *
class Character(Sprite):
    def __init__(self, type, x,y, ammo, grenades):
        super().__init__()
        self.alive = True
        self.health = 100
        self.max_health = 100
        self.ammo = ammo
        self.grenades = grenades
        self.animation_types = os.listdir(f"assets/images/{type}")
        self.all_images = {}
        for animation in self.animation_types:
            temp = []
            num_of_images = len(os.listdir(f"assets/images/{type}/{animation}"))
            for i in range(num_of_images):
                img = pygame.image.load(f"assets/images/{type}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 2, img_h * 2))
                temp.append(img)
            self.all_images[animation] = temp
        self.image_number = 0
        self.action = "Idle"
        self.image = self.all_images[self.action][self.image_number]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_image_change_time = 0
        self.flip = False
        self.yspeed = 0
        self.in_air = False
        
    def draw(self, screen):
        self.animation()
        img =  self.all_images[self.action][self.image_number]
        img = pygame.transform.flip(img, self.flip, False)
        screen.blit(img, self.rect)
        
    def animation(self):
        if pygame.time.get_ticks() - self.last_image_change_time>100:
            self.last_image_change_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.all_images[self.action]):
                self.image_number = 0
        
    def change_animation(self, new_animation):
        if new_animation != self.action:
            self.action = new_animation
            self.image_number = 0
            self.last_image_change_time = pygame.time.get_ticks()   
            
            
    def move(self, moving_left, moving_right)  :
        dx = 0
        dy = 0
        if moving_left:
            self.flip = True
            dx -= 5 
        if moving_right:
            self.flip = False
            dx += 5 
        dy += self.yspeed
        self.yspeed += 1    
        
        if self.rect.bottom + dy >= 400:
            self.in_air = False
            self.yspeed = 0
            dy = 400 - self.rect.bottom
        self.rect.x += dx
        self.rect.y += dy
