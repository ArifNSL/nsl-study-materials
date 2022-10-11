import pygame
BLACK= (0, 0, 0)

class Brick(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        #color, position, height, width
        #set bg set to transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        #draw brick rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        #fetch the rectangle object that has the dimension of the image
        self.rect = self.image.get_rect()