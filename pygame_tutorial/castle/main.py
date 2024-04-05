from constants import *
from world import World
from castle import Castle
from mousepointer import MousePointer
bullet_group = pygame.sprite.Group()
new_castle = Castle()

game_world = World(bg_img)
mouse = MousePointer()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    game_world.draw(screen) 
    mouse.draw(screen)
    new_castle.draw(screen) 
    new_castle.fire(bullet_group)
    bullet_group.update()         
    bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)