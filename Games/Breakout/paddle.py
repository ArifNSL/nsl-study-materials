import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        #call the parent class constructor
        super().__init__()
        
        #color, width, height
        #transparent bacground color
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        #Draw paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        #fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        
        
    def moveLeft(self, pixels):
        self.rect.x -= pixels
            
        #constrain inside the screen
        if self.rect.x < 0:
                self.rect.x = 0
                
    def moveRight(self, pixels):
        self.rect.x += pixels
            
        #inside the screen
        if self.rect.x > 700:
            self.rect.x = 700
            
            
    def moveUp(self, pixels):
        self.rect.y -= pixels
            
        #inside the screen
        if self.rect.y < 40:
            self.rect.y = 40
            
            
    def moveDown(self, pixels):
        self.rect.y += pixels
            
        #inside the screen
        if self.rect.y > 590:
            self.rect.y = 590