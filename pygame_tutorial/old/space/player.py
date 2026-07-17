from pygame.sprite import Sprite
import pygame
from constants import *
from player_bullet import PlayerBullet


class Player(Sprite):
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/player_ship.png")
        self.rect = self.image.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 32))

        self.lives = 3
        self.velocity = 5
        self.bullet_group = bullet_group
        self.hit_sound = pygame.mixer.Sound("assets/player_hit.wav")
        self.fire_sound = pygame.mixer.Sound("assets/player_fire.wav")

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.velocity

    def fire(self):
        if len(self.bullet_group) < 2:################
            self.fire_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
