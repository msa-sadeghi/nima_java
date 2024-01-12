import random

import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Burger Dog")


FPS = 60
clock = pygame.time.Clock()

PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
BURGER_STARTING_VELOCITY = 3
BURGER_ACCELERATION = 0.5
STARTING_BOOST_LEVEL = 100


score = 0
burger_points = 0
burger_eaten = 0


player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_STARTING_LIVES
boost_level = STARTING_BOOST_LEVEL
burger_velocity = BURGER_STARTING_VELOCITY

ORANGE = (246, 170, 54)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font("assets/fonts/WashYourHand.ttf", 32)

points_text = font.render(f"Burger Points: {burger_points}", True, ORANGE)
points_text_rect = points_text.get_rect()
points_text_rect.topleft = (10, 10)

score_text = font.render(f"Score: {score}", True, ORANGE)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10, 50)

title_text = font.render("Burger Dog", True, ORANGE)
title_text_rect = title_text.get_rect()
title_text_rect.centerx = WINDOW_WIDTH/2
title_text_rect.y = 10

eaten_text = font.render(f"Burgers Eaten: {burger_eaten}", True, ORANGE)
eaten_text_rect = eaten_text.get_rect()
eaten_text_rect.centerx = WINDOW_WIDTH/2
eaten_text_rect.y = 50

lives_text = font.render(f"Lives: {player_lives}", True, ORANGE)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WINDOW_WIDTH - 10, 10)

boost_text = font.render(f"Boost: {boost_level}", True, ORANGE)
boost_text_rect = boost_text.get_rect()
boost_text_rect.topright = (WINDOW_WIDTH - 10, 50)

bark_sound = pygame.mixer.Sound("assets/sounds/bark_sound.wav")
miss_sound = pygame.mixer.Sound("assets/sounds/miss_sound.wav")
pygame.mixer.music.load("assets/sounds/bd_background_music.wav")

player_temp_image_load = pygame.image.load("assets/images/dog.png")
player_image_left = pygame.transform.scale(player_temp_image_load, (64, 64))
player_image_right = pygame.transform.flip(player_image_left, True, False)


player_image = player_image_right
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH/2
player_rect.bottom = WINDOW_HEIGHT


big_burger_image = pygame.image.load("assets/images/burger.png")
big_burger_image = pygame.transform.scale(big_burger_image, (64, 64))
burger_image = pygame.transform.scale(big_burger_image, (32, 32))
burger_image_rect = burger_image.get_rect()
burger_image_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -100)


big_burger_image_rect = big_burger_image.get_rect()
big_burger_image_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -100)

pygame.mixer.music.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_velocity
        player_image = player_image_left
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_velocity
        player_image = player_image_right

    if keys[pygame.K_UP] and player_rect.top > 100:
        player_rect.y -= player_velocity
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_velocity

    if keys[pygame.K_SPACE] and boost_level > 0:
        player_velocity = PLAYER_BOOST_VELOCITY
        boost_level -= 1
    else:
        player_velocity = PLAYER_NORMAL_VELOCITY

    burger_points = (WINDOW_HEIGHT - burger_image_rect.y)//50 + 2

    burger_image_rect.y += burger_velocity
    if burger_image_rect.y > WINDOW_HEIGHT:
        burger_image_rect.topleft = (
            random.randint(0, WINDOW_WIDTH - 32), -100)
        player_lives -= 1
        miss_sound.play()

    if player_rect.colliderect(burger_image_rect):
        score += burger_points
        burger_eaten += 1
        bark_sound.play()
        burger_image_rect.topleft = (
            random.randint(0, WINDOW_WIDTH - 32), -100)
        burger_velocity += BURGER_ACCELERATION
        boost_level += 20
        if boost_level > STARTING_BOOST_LEVEL:
            boost_level = STARTING_BOOST_LEVEL

    boost_text = font.render(f"Boost: {boost_level}", True, ORANGE)
    points_text = font.render(f"Burger Points: {burger_points}", True, ORANGE)
    score_text = font.render(f"Score: {score}", True, ORANGE)
    eaten_text = font.render(f"Burgers Eaten: {burger_eaten}", True, ORANGE)
    lives_text = font.render(f"Lives: {player_lives}", True, ORANGE)

    display_surface.fill(BLACK)
    display_surface.blit(points_text, points_text_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(eaten_text, eaten_text_rect)
    display_surface.blit(lives_text, lives_text_rect)
    display_surface.blit(boost_text, boost_text_rect)

    display_surface.blit(player_image, player_rect)
    display_surface.blit(burger_image, burger_image_rect)
    if score > 100:
        display_surface.blit(big_burger_image, big_burger_image_rect)

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
