import pygame
from player import Player
width = 1000
height = 600
clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((width, height))
my_player = Player(100, 300)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if my_player.moving:
        my_player.change_animation('Run')
    else:
        my_player.change_animation('Idle')
    
    screen.fill("black")
    my_player.draw(screen)
    my_player.move()
    pygame.display.update()
    clock.tick(fps)