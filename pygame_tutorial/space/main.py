import pygame
from constants import *
from player import Player
from game import Game
pygame.init()

clock = pygame.time.Clock()
player_bullet_group = pygame.sprite.Group()
my_player = Player(player_bullet_group)
enemy_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()

my_game = Game(my_player, enemy_group,player_bullet_group,enemy_bullet_group)
my_game.start_new_level()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                my_player.fire()
    screen.fill((0,0,0))
    my_player.move()
    my_player.draw(screen)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    enemy_bullet_group.update()################
    enemy_bullet_group.draw(screen)################
    enemy_group.update()
    enemy_group.draw(screen)
    my_game.if_on_edge()
    my_game.check_enemy_hit()
    my_game.draw()################
    pygame.display.update()
    clock.tick(FPS)
