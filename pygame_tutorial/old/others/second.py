from random import randint
from tkinter import font
from numpy import place
import pygame
import sys
import os
pygame.init()


def change_coin_position():
    coin_rect.x = WINDOW_WIDTH + 100
    coin_rect.y = randint(90, WINDOW_HEIGHT - 32)


if getattr(sys, 'frozen', False):
    wd = sys._MEIPASS
else:
    wd = ''
# family_image = pygame.image.load(
#     os.path.join(wd, 'folder', "family.jpg")).convert()
# Create a display surface and set its caption
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
BLACK = (0, 0, 0)
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 30
COIN_STARTING_VELOCITY = 10
COIN_ACCELARATION = 0.5
FPS = 60
clock = pygame.time.Clock()

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY


success_sound = pygame.mixer.Sound('sound_1.wav')
miss_sound = pygame.mixer.Sound('sound_2.wav')


pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1, 0.0)

display_surface = pygame.display.set_mode((WINDOW_WIDTH,
                                           WINDOW_HEIGHT))
pygame.display.set_caption("Second Game")

my_font = pygame.font.Font("AttackGraffiti.ttf", 32)

score_text = my_font.render(f"Score : {score}",
                            True, GREEN, DARK_GREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (90, 16)

title_text = my_font.render("Dragon Game ",
                            False, GREEN,
                            DARK_GREEN)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH/2
title_rect.y = 16

lives_text = my_font.render(f"Lives : {player_lives}", True, GREEN, DARK_GREEN)
lives_rect = score_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH-90, 16)

game_over_text = my_font.render("GAMEOVER", True, GREEN, DARK_GREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


continue_text = my_font.render(
    "Press any key to play again", True, GREEN, DARK_GREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)


dragon_left_image = pygame.image.load(os.path.join(wd,
                                                   '',
                                                   "dragon_left.png"))
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load(
    os.path.join(wd, '', "dragon_right.png"))
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

dragon_image = pygame.image.load("dragon_right.png")
player_rect = dragon_image.get_rect()
player_rect.centerx = 32
player_rect.bottom = WINDOW_HEIGHT

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
change_coin_position()


# The main game loop
running = True
while running:
    # Loop through a list of event objects that have occured
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_DOWN:
        #         player_rect.y += PLAYER_VELOCITY

        #     if event.key == pygame.K_UP:
        #         player_rect.y -= PLAYER_VELOCITY

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_rect.top > 90:
        player_rect.y -= PLAYER_VELOCITY

    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT - 20:
        player_rect.y += PLAYER_VELOCITY

    if keys[pygame.K_LEFT] and player_rect.left > 15:
        player_rect.x -= PLAYER_VELOCITY

    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH - 15:
        player_rect.x += PLAYER_VELOCITY
    # Move the coin from right to left until coin exit from the left side of the screen
    if coin_rect.x < 0:
        player_lives -= 1
        miss_sound.play()
        change_coin_position()
    else:
        coin_rect.x -= coin_velocity

    # check for collisions
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_velocity += COIN_ACCELARATION
        success_sound.play()
        change_coin_position()
    score_text = my_font.render(f"Score : {score}", True, GREEN, DARK_GREEN)
    lives_text = my_font.render(
        f"lives : {player_lives}", True, GREEN, DARK_GREEN)

    if player_lives == 0:
        display_surface.blit(score_text, score_rect)
        display_surface.blit(title_text, title_rect)
        display_surface.blit(lives_text, lives_rect)
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_text_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        is_paused = True

        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.centerx = 32
                    player_rect.bottom = WINDOW_HEIGHT
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    display_surface.fill((0, 0, 0))
    # Blit (copy) a surface object at the given coordinates to our display
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(dragon_left_image,
                         dragon_left_rect)
    display_surface.blit(dragon_right_image,
                         dragon_right_rect)

    pygame.draw.line(display_surface,
                     (255, 255, 255),
                     (0, 64), (WINDOW_WIDTH, 64))
    display_surface.blit(dragon_image, player_rect)
    display_surface.blit(coin_image, coin_rect)

    # Update the display
    pygame.display.update()
    clock.tick(60)
pygame.quit()
