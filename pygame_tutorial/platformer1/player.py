from constants import *
from pygame.sprite import Sprite
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.right_images = []
        self.left_images = []
        self.idle_right = []
        self.idle_left = []
        # این حلقه برای اضافه کردن تصاویر بازیکن در حال حرکت به سمت راست و چپ نوشته شده است
        for i in range(1,9):
            temp_img = pygame.image.load(f"assets/boy/Run ({i}).png")
            image = pygame.transform.scale(temp_img, (temp_img.get_width() * 0.2, temp_img.get_height()*0.2))
            self.right_images.append(image)
            image = pygame.transform.flip(image, True, False)
            self.left_images.append(image)

        # این حلقه برای لود کردن و اضافه کردن عکس های بازیکن که بدون حرکت است می باشد
        for i in range(1,10):
            img = pygame.image.load(f"assets/boy/Idle ({i}).png")
            img = pygame.transform.scale(img, (img.get_width() * 0.2, img.get_height()*0.2))
            self.idle_right.append(img)
            img = pygame.transform.flip(img, True, False)
            self.idle_left.append(img)

        
        self.frame_index = 0
        self.counter = 0
        self.last_animation_time = pygame.time.get_ticks()
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.velocity = 5
        self.direction = 1
        self.moving = False


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.moving = True
            self.direction = 1
            self.rect.x += self.velocity
        if keys[pygame.K_LEFT]:
            self.moving = True
            self.direction = -1
            self.rect.x -= self.velocity
        
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.moving = False

     
        self.animation()


    def animation(self):
        # ANIMATION_COOLDOWN = 4
        # self.counter += 1
        # if self.counter > ANIMATION_COOLDOWN:
        if pygame.time.get_ticks() - self.last_animation_time > 100:
            self.last_animation_time = pygame.time.get_ticks()
            self.frame_index += 1
            # self.counter = 0
        if self.frame_index >= len(self.right_images) - 1:
            self.frame_index = 0
        if self.direction == 1:
            if self.moving:
                self.image = self.right_images[self.frame_index]
            else:
                self.image = self.idle_right[self.frame_index]
        if self.direction == -1:
            if self.moving:
                self.image = self.left_images[self.frame_index]
            else:
                self.image = self.idle_left[self.frame_index]
