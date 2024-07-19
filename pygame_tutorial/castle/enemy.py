import pygame.time
from pygame.sprite import Sprite
class Enemy(Sprite):
    def __init__(self, x, y, all_images, health,speed, group):
        Sprite.__init__(self)
        self.all_images = all_images
        self.image_number = 0
        self.action = 0
        self.image = self.all_images[self.action][self.image_number]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = health
        self.max_health = health
        self.alive = True
        self.speed = speed
        self.last_image_chng = pygame.time.get_ticks()
        self.last_injury_time = pygame.time.get_ticks()
        self.last_tower_injury_time = pygame.time.get_ticks()
        group.add(self)
        self.hit_sound = pygame.mixer.Sound("assets/hit.wav")
    def update(self, castle, bullet_group,screen, f, tower_group):

        self.move(castle, bullet_group, tower_group)
        self.next_costume()
        if self.alive:
            # if enemy health is less than or equal to half -> text color : red
            # else -> text color : blue
            # excerise 28  book: PythonProgrammingExercisesGentlyExplained
            # show enemy health
            if self.health <= self.max_health/2:
                text = f.render(f"{self.health}", True, (255,0,0))
            else:
                text = f.render(f"{self.health}", True, (0,0,255))
                
            rect = text.get_rect(center=(self.rect.centerx - self.rect.size[0]/6, self.rect.top))
            screen.blit(text, rect)

    def move(self, castle, bullet_group, tower_group):
        if self.alive:
            collided_tower = pygame.sprite.spritecollideany(self, tower_group)
            if collided_tower:
                if pygame.time.get_ticks() - self.last_tower_injury_time > 1000:
                    self.last_tower_injury_time = pygame.time.get_ticks()
                    collided_tower.health -= 20
                    if collided_tower.health <= 0:
                        collided_tower.health = 0
                    
                
            if self.rect.right >= castle.rect.left:
                self.change_action(1)
            if pygame.sprite.spritecollide(self, bullet_group, True)    :
                self.health -= 1
                self.hit_sound.play()
                
                
            if self.health <= 0:
                self.change_action(2)
                self.alive = False
                castle.money += 200
                castle.score += 200
                
            if self.action == 0:
                self.rect.x += self.speed
            if self.action == 1:
                if pygame.time.get_ticks() - self.last_injury_time > 2500:
                    self.last_injury_time = pygame.time.get_ticks()
                    castle.health -= 100
    
            
    
    def change_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
    
    def next_costume(self):
        self.image = self.all_images[self.action][self.image_number]
        if pygame.time.get_ticks() - self.last_image_chng > 100:
            self.last_image_chng = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.all_images[self.action]):
                if self.action == 2:
                    self.image_number = len(self.all_images[self.action]) - 1
                else:
                    self.image_number = 0
