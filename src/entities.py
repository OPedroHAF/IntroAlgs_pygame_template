import pygame
import config
import random

class Player():
    def __init__(self, hp, spd, starting_x, starting_y, width, height):
        self.hp = hp
        self.spd = spd
        self.rect = pygame.Rect(starting_x, starting_y, width, height)
        self.image = config.PLAYER_IMAGE
        self.is_alive = True
    
    def move(self, keys, dt):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.x > 0:
            self.rect.x -= self.spd * dt
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.x < config.SCREEN_WIDTH - config.PLAYER_WIDTH:
            self.rect.x += self.spd * dt
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.y > 0:
            self.rect.y -= self.spd * dt
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.y < config.SCREEN_HEIGHT - config.PLAYER_HEIGHT:
            self.rect.y += self.spd * dt
    
    def take_damage(self, damage):
        self.hp = max(self.hp - damage, 0)

class Meteor():
    def __init__(self, hp, spd, damage):
        self.hp = hp
        self.spd = spd
        self.damage = damage

        if config.METEOR_FRAMES:
            self.width, self.height = config.METEOR_FRAMES[0].get_size()
        else:
            self.width = config.METEOR_WIDTH
            self.height = config.METEOR_HEIGHT

        random_x = random.randint(50, config.SCREEN_WIDTH - self.width - 50)
        starting_y = -self.height

        self.rect = pygame.Rect(random_x, starting_y, self.width, self.height)

        self.current_frame = 0
        self.animation_timer = 0.0
        self.animation_spd = 0.2

    def move(self, dt):
        self.rect.y+= self.spd * dt

        self.animation_timer += dt
        if self.animation_timer >= self.animation_spd:
            self.animation_timer = 0.0
            self.current_frame = (self.current_frame + 1) % 5
    
    def take_damage(self, amount):
        self.hp -= amount

class Bullet():
    def __init__(self, spd, x, y, width, height):
        self.spd = spd
        self.width = width
        self.height = height
        
        starting_x = x + (config.PLAYER_WIDTH // 2) - (self.width // 2)
        starting_y = y

        self.rect = pygame.Rect(starting_x, starting_y, self.width, self.height)

    def move(self, dt):
        self.rect.y -= self.spd * dt


        



