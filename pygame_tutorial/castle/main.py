import pygame.time

from constants import *
from world import World
from castle import Castle
from mousepointer import MousePointer
from enemy import Enemy
import random
from button import Button


bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
new_castle = Castle()
MAX_DIFFICULTY = 5
level_difficulty = 0
game_world = World(bg_img)
mouse = MousePointer()
last_spawn_time = pygame.time.get_ticks()

font = pygame.font.SysFont("arial", 32)
font22 = pygame.font.SysFont("arial", 18)

# show text in screen
def show_text(txt, x,y, font):
    t = font.render(txt, True, (255,10,10))
    r = t.get_rect(center =(x,y))
    screen.blit(t, r)
    

level_completed = False
level = 1
repair_button = Button(x=SCREEN_WIDTH - 150, y=10, image=repair_img)
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    i = 1
    if level_difficulty < MAX_DIFFICULTY:
        if pygame.time.get_ticks() - last_spawn_time > 3000:
            last_spawn_time = pygame.time.get_ticks()
            j = random.randrange(len(all_enemies_types))
            Enemy(-100,  SCREEN_HEIGHT - i * 400, all_enemies_images[j], all_enemies_healths[j], i * 4, enemy_group)
            level_difficulty += all_enemies_healths[j]
            i += 1
    game_world.draw(screen)
    # check if all enemies spawned
    if level_difficulty >= MAX_DIFFICULTY:
        enemies = 0
        # check number of alive enemies
        for enemy in enemy_group:
            if enemy.alive:
                enemies += 1
        if enemies == 0 and not level_completed:
            level_completed = True
            level_completed_time = pygame.time.get_ticks()
            
        if level_completed:
            show_text("LEVEL COMPLETED", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, font)
            if pygame.time.get_ticks() - level_completed_time > 2000:
                level_completed_time = pygame.time.get_ticks()
                enemy_group.empty()
                bullet_group.empty()
                level_difficulty = 0
                MAX_DIFFICULTY *= 1.3
                level_completed = False
                level += 1
    mouse.draw(screen)
    repair_button.draw(screen)
    if repair_button.click():
        
        new_castle.repair()
    show_text(f"Health: {new_castle.health}", SCREEN_WIDTH - 230, SCREEN_HEIGHT-180, font)
    show_text(f"Score: {new_castle.score}", 60, 20, font)
    show_text(f"Money: {new_castle.money}", 310, 20, font)
    show_text(f"Level: {level}", 60, 60, font)
    show_text("1000", repair_button.rect.centerx, repair_button.rect.bottom + 20, font22)
    new_castle.draw(screen) 
    new_castle.fire(bullet_group)
    bullet_group.update()         
    bullet_group.draw(screen)
    enemy_group.update(new_castle, bullet_group, screen, font)
    enemy_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)