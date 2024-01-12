from constants import *
from world import World
from player import Player
pygame.init()

bg_image = pygame.image.load("assets/background.png")
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
w = World(bg_image)

player1_image = pygame.image.load("assets/boy/Idle (1).png")
player1_width = player1_image.get_width()
player1_height = player1_image.get_height()
player1_image = pygame.transform.scale(player1_image, (player1_width * 0.2, player1_height * 0.2))


player1_rect = player1_image.get_rect()
player1_rect = pygame.Rect(player1_rect.x + 40, player1_rect.y + 30, player1_width * 0.2 , player1_height * 0.2 )


p1 = Player(player1_image,player1_rect, 100, 700, 2)

player2_image = pygame.image.load("assets/guy/guy1.png")
player2_width = player2_image.get_width()
player2_height = player2_image.get_height()
player2_image = pygame.transform.scale(player2_image, (player2_width * 0.7, player2_height * 0.7))
player2_rect = player2_image.get_rect()

p2 = Player(player2_image,player2_rect, 700, 700, 1)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    w.draw()
    p1.draw()
   

    
    p2.draw()
    pygame.display.update()
