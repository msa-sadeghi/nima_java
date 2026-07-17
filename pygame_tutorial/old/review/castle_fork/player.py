import pygame
from pygame.sprite import Sprite
class Player(Sprite):
    def __init__(self,type, x,y):
        super().__init__()
        self.animation_types = ("walk", "attack", "death")
        self.all_images = []
        for anim in self.animation_types:
            temp = []
            for i in range(20):
                img = pygame.image.load(f"assets/enemies/{type}/{anim}/{i}.png")
                img = pygame.transform.scale(img, (200, 150))
                temp.append(img)
            self.all_images.append(temp)
        self.image = self.all_images[0][0]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.image_number = 0
        self.moving_or_not = False
    def draw(self, screen):
        self.image = self.all_images[0][self.image_number]
        screen.blit(self.image, self.rect)
    def animation(self):
        self.image_number += 1
        if self.image_number >= len(self.all_images[0]):
            self.image_number = 0
            
    def move(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moving_or_not = True
        if keys[pygame.K_RIGHT]:
            self.moving_or_not = True
        if not  keys[pygame.K_LEFT]   and   not  keys[pygame.K_RIGHT]:
            self.moving_or_not = False
            
            
        
                
            
        