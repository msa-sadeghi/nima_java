import pygame
import random
from monster import Monster
from knight import Knight

WINDOW_WIDTH = 800
WINDOW_HEIGTH = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("test")

FPS = 60
clock = pygame.time.Clock()

monster_group = pygame.sprite.Group()
for i in range(12):
    monster = Monster(i*66, 10)
    monster_group.add(monster)
player_group = pygame.sprite.Group()
knight = Knight(500, 500)
player_group.add(knight)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.fill((0,0,0))
    monster_group.draw(display_surface)
    player_group.draw(display_surface)
    monster_group.update()
    player_group.update()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
