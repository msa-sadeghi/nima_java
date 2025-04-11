from pygame.sprite import Sprite
import pygame
import os
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.all_images = {}
        idle_images = []
        run_images = []
        images_names = os.listdir("./images")
        for im in images_names:
            if im.find("Idle")!=-1:
                img = pygame.image.load(f"./images/{im}")
                img = pygame.transform.scale_by(img, 0.5)
                idle_images.append(img)
            elif im.find("Run")!=-1:
                img = pygame.image.load(f"./images/{im}")
                img = pygame.transform.scale_by(img, 0.5)
                run_images.append(img)
        self.all_images["Idle"] = idle_images
        self.all_images["Run"] = run_images

        self.costume_number = 0
        self.image = self.all_images['Idle'][self.costume_number]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_image_time = pygame.time.get_ticks()
        self.action = "Idle"
        self.moving = False
        self.flip = False
        self.yspeed = 0
    def draw(self, screen):
        img = self.all_images[self.action][self.costume_number]
        img = pygame.transform.flip(img, self.flip, False)
        screen.blit(img, self.rect)
        self.animation()


    def animation(self):
        if pygame.time.get_ticks() - self.last_image_time >= 100:
            self.last_image_time = pygame.time.get_ticks()
            self.costume_number += 1
            if self.costume_number >= len(self.all_images[self.action]):
                self.costume_number = 0
    
    def change_animation(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.costume_number = 0
    
    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moving = True
            self.flip = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.moving = True
            self.flip = False
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving = False
        if keys[pygame.K_UP]:
            self.yspeed = -15
        self.yspeed += 1
        dy += self.yspeed
        if self.rect.bottom + dy >= 500:
            dy = 500 -self.rect.bottom
            self.yspeed = 0
        self.rect.x += dx
        self.rect.y += dy





