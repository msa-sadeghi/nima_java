import pygame.time

from constants import *
from world import World
from castle import Castle
from mousepointer import MousePointer
from enemy import Enemy
import random
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
new_castle = Castle()
MAX_DIFFICULTY = 10
level_difficulty = 0
game_world = World(bg_img)
mouse = MousePointer()
last_spawn_time = pygame.time.get_ticks()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    i = 1
    if level_difficulty < MAX_DIFFICULTY:
        print("inside update function")
        if pygame.time.get_ticks() - last_spawn_time > 3000:
            last_spawn_time = pygame.time.get_ticks()
            j = random.randrange(len(all_enemies_types))
            Enemy(-100,  SCREEN_HEIGHT - i * 400, all_enemies_images[j], all_enemies_healths[j], i * 2, enemy_group)
            level_difficulty += all_enemies_healths[j]
            i += 1

    game_world.draw(screen)
    mouse.draw(screen)
    new_castle.draw(screen) 
    new_castle.fire(bullet_group)
    bullet_group.update()         
    bullet_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)