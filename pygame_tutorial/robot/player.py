from pygame.sprite import Sprite
import pygame
import os

class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.actions = os.listdir("png")
        self.all_images = {}
        for action in self.actions:
            images = os.listdir(f"png/{action}")
            temp = []
            for image in images:
                img = pygame.image.load(f"png/{action}/{image}")
                img = pygame.transform.scale_by(img, 0.3)
                temp.append(img)

            self.all_images[action] = temp
        self.action = "Idle"
        self.frame_index = 0
        self.image = self.all_images[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_update_time = pygame.time.get_ticks()
        self.flip = False
        self.idle = True
        self.direction = 1
        self.slide = False
        self.in_air = False
        self.gravity = 0.5
        self.shoot = False

    def draw(self, screen):
        screen.blit(
            pygame.transform.flip(self.image, self.flip, False)
            , self.rect)
        self.animation()
    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.flip  = True
            self.direction = -1
            self.idle = False
            dx += -5
        elif keys[pygame.K_RIGHT]:
            self.flip = False
            self.direction = 1
            self.idle = False
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True

        if keys[pygame.K_DOWN]:
            self.slide = True
            dx += self.direction * 5

        else:
            self.slide = False
        if keys[pygame.K_UP] and not self.in_air:
            self.in_air = True
            self.gravity = -10
        if keys[pygame.K_SPACE]:
            self.shoot = True
        else:
            self.shoot = False
    
        dy += self.gravity
        self.gravity += 0.5
        if self.rect.bottom + dy >= 600:
            self.in_air = False
            dy = 600 - self.rect.bottom
            self.gravity = 0
        self.rect.x += dx
        self.rect.y += dy

    def animation(self):
        self.image = self.all_images[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.last_update_time >= 100:
            self.frame_index += 1
            self.last_update_time = pygame.time.get_ticks()
            if self.frame_index >= len(self.all_images[self.action]):
                self.frame_index = 0

    def change_animation(self,  new):
        if new != self.action:
            self.action = new
            self.frame_index = 0
            self.last_update_time = pygame.time.get_ticks()
      