import pygame.draw

from constants import *
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.right_images = []
        self.left_images = []
        self.idle_right = []
        self.idle_left = []
        # این حلقه برای اضافه کردن تصاویر بازیکن در حال حرکت به سمت راست و چپ نوشته شده است
        for i in range(1, 5):
            # temp_img = pygame.image.load(f"assets/boy/Run ({i}).png")
            # image = pygame.transform.scale(temp_img, (temp_img.get_width() * 0.2, temp_img.get_height() * 0.2))
            image = pygame.image.load(f"assets/boy/guy{i}.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.5, image.get_height() * 0.5))
            self.right_images.append(image)
            image = pygame.transform.flip(image, True, False)
            self.left_images.append(image)

        # این حلقه برای لود کردن و اضافه کردن عکس های بازیکن که بدون حرکت است می باشد
        # for i in range(1, 10):
        #     img = pygame.image.load(f"assets/boy/Idle ({i}).png")
        #     img = pygame.transform.scale(img, (img.get_width() * 0.2, img.get_height() * 0.2))
        #     self.idle_right.append(img)
        #     img = pygame.transform.flip(img, True, False)
        #     self.idle_left.append(img)

        self.frame_index = 0
        self.counter = 0
        self.last_animation_time = pygame.time.get_ticks()
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = 5
        self.direction = 1
        self.moving = False
        self.vel_y = 0
        self.ghost_image = pygame.image.load("assets/img/ghost.png")
        self.alive = True
        self.in_air = False
        self.jumped = False

    def update(self, tiles_map, enemy_group):
        # pygame.draw.rect(SCREEN, (190, 30, 230), self.rect, 5)
        # if self.direction == 1:
        #     rect = pygame.Rect(self.rect.x + 50, self.rect.y + 15, self.image.get_width()- 80, self.image.get_height()-24)
        # if self.direction == -1:
        #     rect = pygame.Rect(self.rect.x + 30, self.rect.y + 15, self.image.get_width()- 80, self.image.get_height()-24)
        # pygame.draw.rect(SCREEN, (30, 190, 230), rect, 5)

        dx = 0
        dy = 0
        
        if self.alive:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.moving = True
                self.direction = 1
                dx += self.velocity
            if keys[pygame.K_LEFT]:
                self.moving = True
                self.direction = -1
                dx -= self.velocity

            if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                self.moving = False

            if keys[pygame.K_SPACE] and not self.jumped and not self.in_air:
                self.vel_y = -15
                self.jumped = True
                self.in_air = True
            if not keys[pygame.K_SPACE]:
                self.jumped = False
                
            self.vel_y += 1
            dy += self.vel_y

            for tile in tiles_map:
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.image.get_width(), self.image.get_height()):
                    dx = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.image.get_width(), self.image.get_height()):
                    
                    if self.vel_y < 0:
                        self.vel_y = 0
                        dy = tile[1].bottom - self.rect.top
                    elif self.vel_y > 0:
                        self.vel_y = 0
                        dy = tile[1].top - self.rect.bottom
                        self.in_air = False
            self.animation()
        
            if pygame.sprite.spritecollide(self, enemy_group, False):
                self.alive = False
                
        if not self.alive:
            self.image = self.ghost_image
            if self.rect.top > 200:
                self.rect.y -= 5
        
        self.rect.x += dx
        self.rect.y += dy
        # if self.rect.bottom >= SCREEN_HEIGHT:
        #     self.rect.bottom = SCREEN_HEIGHT

    def animation(self):
        # ANIMATION_COOLDOWN = 4
        # self.counter += 1
        # if self.counter > ANIMATION_COOLDOWN:
        if pygame.time.get_ticks() - self.last_animation_time > 100:
            self.last_animation_time = pygame.time.get_ticks()
            self.frame_index += 1
            # self.counter = 0
        if self.frame_index >= len(self.right_images) - 1:
            self.frame_index = 0
        if self.direction == 1:
            if self.moving:
                self.image = self.right_images[self.frame_index]
            # else:
            #     self.image = self.idle_right[self.frame_index]
        if self.direction == -1:
            if self.moving:
                self.image = self.left_images[self.frame_index]
            # else:
            #     self.image = self.idle_left[self.frame_index]
