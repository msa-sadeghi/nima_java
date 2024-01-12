from constants import *
from world import World
from levels.level1 import WORLD_DATA

player_group = pygame.sprite.Group()

world = World(WORLD_DATA,player_group)

running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    world.draw()
    player_group.update()
    player_group.draw(SCREEN)
    pygame.display.update()
    CLOCK.tick(FPS)