import pygame
from pygame.locals import *
pygame.init()
SCREEN = pygame.display.set_mode()
SCREEN_WIDTH = SCREEN.get_width()
SCREEN_HEIGHT = SCREEN.get_height()
print(SCREEN_WIDTH, SCREEN_HEIGHT)

TILE_SIZE = 32
COLS = SCREEN_WIDTH//TILE_SIZE
ROWS = SCREEN_HEIGHT//TILE_SIZE

print(COLS, ROWS)

BG_PIC = pygame.image.load("assets/background.png")
BG_PIC = pygame.transform.scale(BG_PIC,(SCREEN_WIDTH,SCREEN_HEIGHT))


DIRT_IMAGE = pygame.image.load("assets/dirt.png")
GRASS_IMAGE = pygame.image.load("assets/grass.png")
WATER_IMAGE = pygame.image.load("assets/water.png")
ENEMY_IMAGE = pygame.image.load("assets/img/blob.png")
RESTART_BTN_IMAGE = pygame.image.load("assets/img/restart_btn.png")
COIN_IMAGE = pygame.transform.scale(pygame.image.load("assets/img/coin.png"),(32,32))

FPS = 60
CLOCK = pygame.time.Clock()
