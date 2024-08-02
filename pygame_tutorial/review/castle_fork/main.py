import pygame
# from player import Player
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
FPS = 60

# p = Player(100, 200)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    # p.draw(screen)   
    # p.animation()    
    pygame.display.update()
    clock.tick(FPS)
    
    