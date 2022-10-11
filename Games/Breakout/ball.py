import pygame
from random import randint, choice
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    
    
    def __init__(self, color, width, height):
        
        super().__init__()
        
        #color, width, height
        #background color, set to transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.mask = pygame.mask.from_surface(self.image)
        
        #rectangular ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4, 8), randint(-4, 4)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = choice([i for i in range(-4, 4) if i != 0])