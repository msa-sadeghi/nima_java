import pygame
from player import Player
import random
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
FPS = 60
player_group = pygame.sprite.Group()
player_types = ("goblin" ,"red_goblin" ,"purple_goblin" , "knight")
x = 0
y = 200
for i in range(4):
    # p = Player(player_types[i % len(player_types)], x, y)
    p = Player(player_types[random.randrange(len(player_types))], x, y)
    player_group.add(p)
    x += 200
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    for player in player_group:
        if p.moving_or_not:
            player.animation()    
        player.draw(screen)
        player.move()
    pygame.display.update()
    clock.tick(FPS)
    
