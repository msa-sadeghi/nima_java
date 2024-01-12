from random import choice, randint
import pygame
from config import WINDOW_HEIGHT, WINDOW_WIDTH

from monster import Monster


class Game:
    def __init__(self, player, monster_group) -> None:
        self.score = 0
        self.round_number = 0

        self.round_time = 0

        self.next_level_sound = pygame.mixer.Sound("assets/next_level.wav")

        self.player = player
        self.monster_group = monster_group
        self.font = pygame.font.Font("assets/Abrushow.ttf", 24)

        blue_monster = pygame.image.load("assets/blue_monster.png")
        green_monster = pygame.image.load("assets/green_monster.png")
        purple_monster = pygame.image.load("assets/purple_monster.png")
        yellow_monster = pygame.image.load("assets/yellow_monster.png")

        self.target_monsters_images = [
            blue_monster, green_monster, purple_monster, yellow_monster]

        self.taget_monster_type = randint(0, 3)
        self.target_monster = self.target_monsters_images[self.taget_monster_type]
        self.target_monster_rect = self.target_monster.get_rect()
        self.target_monster_rect.bottom = 100
        self.target_monster_rect.centerx = WINDOW_WIDTH/2

    def update(self, screen):
        collided_monster = pygame.sprite.spritecollideany(
            self.player, self.monster_group)
        if collided_monster:
            if collided_monster.type == self.taget_monster_type:
                collided_monster.remove(self.monster_group)
                self.player.catch_sound.play()
                if self.monster_group:
                    self.change_target()
                else:
                    self.start_new_round()
            else:
                self.player.lives -= 1
                self.player.reset()
                if self.player.lives <= 0:
                    self.pause_game(screen)

    def pause_game(self, screen):
        # استاپ کردن بازی بعد از گیم آور شدن
        game_over_text = self.font.render(
            "Game Over, Press any Key to continue...", True, (255, 255, 255))
        game_over_text_rect = game_over_text.get_rect()
        game_over_text_rect.centerx = WINDOW_WIDTH/2
        game_over_text_rect.centery = WINDOW_HEIGHT/2
        # پاک کردن صفحه
        screen.fill((0, 0, 0))
        # نمایش دادن متن گیم اور
        screen.blit(game_over_text, game_over_text_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # اگر بعد از استاپ شدن، بازیکن بخواهد از ابتدا بازی کند
                    is_paused = False
                    self.score = 0
                    self.player.lives = 5
                    self.player.warps = 2
                    self.player.reset()
                    self.round_number = 0
                    # اگر مانستری از این مرجله باقی مانده است حذف شود
                    for monster in self.monster_group:
                        self.monster_group.remove(monster)
                    # مرحله جدید شروع شود
                    self.start_new_round()
                # اگر در زمان استاپ شدن بازی، بازیکن بخواهد بازی را ببندد بتواند
                if event.type == pygame.QUIT:
                    is_paused = False
                    exit()

    def change_target(self):
        new_target = choice(self.monster_group.sprites())
        self.taget_monster_type = new_target.type
        self.target_monster = new_target.image

    def draw(self, display_surface):

        COLORS = (
            (26, 186, 239),  # blue
            (75, 188, 42),  # green
            (238, 81, 254),  # purple
            (245, 158, 24)  # yellow
        )

        score_text = self.font.render(
            f"Score:  {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)
        lives_text = self.font.render(
            f"Lives:  {self.player.lives}", True, (255, 255, 255))
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (5, 35)

        display_surface.blit(self.target_monster, self.target_monster_rect)
        display_surface.blit(score_text, score_rect)
        display_surface.blit(lives_text, lives_rect)
        pygame.draw.rect(display_surface, COLORS[self.taget_monster_type], (
            0, 100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 3)

    def start_new_round(self):
        self.round_number += 1
        for i in range(self.round_number):
            self.monster_group.add(
                Monster(
                    randint(0, WINDOW_WIDTH-64),
                    randint(100, WINDOW_HEIGHT-100),
                    self.target_monsters_images[0],
                    0
                )
            )
            self.monster_group.add(
                Monster(
                    randint(0, WINDOW_WIDTH-64),
                    randint(100, WINDOW_HEIGHT-100),
                    self.target_monsters_images[1],
                    1
                )
            )
            self.monster_group.add(
                Monster(
                    randint(0, WINDOW_WIDTH-64),
                    randint(100, WINDOW_HEIGHT-100),
                    self.target_monsters_images[2],
                    2
                )
            )
            self.monster_group.add(
                Monster(
                    randint(0, WINDOW_WIDTH-64),
                    randint(100, WINDOW_HEIGHT-100),
                    self.target_monsters_images[3],
                    3
                )
            )
        self.next_level_sound.play()
