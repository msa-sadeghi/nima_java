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

next_level_time = pygame.time.get_ticks()

def draw_text(text, color, x,y, font):
    t = font.render(text, True, color)
    r = t.get_rect(topleft=(x,y))
    SCREEN.blit(t, r)



MAX_LEVEL = 10
if os.path.exists(f"levels/level{level}"):
    f = open(f"levels/level{level}", 'rb')
    WORLD_DATA = pickle.load(f)
else:    
    WORLD_DATA = []
    
    
def next_level():
    player_group.empty()
    enemy_group.empty()
    door_group.empty()
    coin_group.empty()
    if os.path.exists(f"levels/level{level}"):
        f = open(f"levels/level{level}", 'rb')
        WORLD_DATA = pickle.load(f)
    else:    
        WORLD_DATA = []
    return World(WORLD_DATA,player_group, enemy_group,door_group,coin_group)
f = pygame.font.SysFont("Arial", 36)        
f24 = pygame.font.SysFont("Arial", 24)        
next_level_text =  f.render(f"welcome to level {level}", True, (255,0,0))
next_level_rect = next_level_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))  

world = World(WORLD_DATA,player_group, enemy_group,door_group,coin_group)
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    next_level_text =  f.render(f"welcome to level {level}", True, (255,0,0))
    world.draw()
    draw_text(f"Score: {player_group.sprites()[0].score}", (210, 190, 210), 10, 7, f24)
    door_group.draw(SCREEN)
    player_group.update(world.tiles_map, enemy_group,door_group)
    player_group.draw(SCREEN)
    if not player_group.sprites()[0].alive:
        restart_button.draw()  
    elif  player_group.sprites()[0].next_level:
        next_level_time = pygame.time.get_ticks()
        level += 1
        world = next_level()
          
    else:    
        enemy_group.update()
        
    if pygame.time.get_ticks() - next_level_time < 2000:
        print(f"level{level}")
        SCREEN.blit(next_level_text, next_level_rect)
        
    enemy_group.draw(SCREEN)
    coin_group.update()
    coin_group.draw(SCREEN)
    pygame.display.update()
    CLOCK.tick(FPS)
