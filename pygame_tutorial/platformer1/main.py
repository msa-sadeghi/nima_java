from constants import *
from world import World

from button import Button
import os
import pickle
restart_button = Button(RESTART_BTN_IMAGE, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
level = 1
if os.path.exists(f"levels/level{level}"):
    f = open(f"levels/level{level}", 'rb')
    WORLD_DATA = pickle.load(f)
else:    
    WORLD_DATA = []

world = World(WORLD_DATA,player_group, enemy_group,door_group,coin_group)
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    world.draw()
    door_group.draw(SCREEN)
    player_group.update(world.tiles_map, enemy_group,door_group)
    player_group.draw(SCREEN)
    if not player_group.sprites()[0].alive:
        restart_button.draw()      
    else:    
        enemy_group.update()
    enemy_group.draw(SCREEN)
    coin_group.update()
    coin_group.draw(SCREEN)
    pygame.display.update()
    CLOCK.tick(FPS)
