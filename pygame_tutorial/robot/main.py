import pygame
from player import Player
pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")


my_player = Player(100, 300)
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    if my_player.shoot:
        my_player.change_animation('Shoot')
    elif my_player.in_air:
        my_player.change_animation('Jump')
    elif my_player.slide:
        my_player.change_animation('Slide')
    elif my_player.idle:
        my_player.change_animation('Idle')
    else:
        my_player.change_animation('Run')
    my_player.draw(screen)
    my_player.move()
    pygame.display.update()
    clock.tick(FPS)