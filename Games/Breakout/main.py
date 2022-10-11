import pygame

#Let's import the Paddle Class
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()

#----------------BGM-----------------#
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Sounds/bgm.mp3')
pygame.mixer.music.play(-1) #-1 is loop forever. 0 is once


#define colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
LIGHTGREEN = (153, 255, 51)
GREEN = (0, 255, 0)

score = 0
lives = 5

size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout-1")


#all Sprites
all_sprites_list = pygame.sprite.Group()

#create paddle---------------------
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 590

#create ball--------------
ball = Ball(WHITE, 10, 10)
ball.rect.x = 350
ball.rect.y = 195

#create brick wall----------------
all_bricks = pygame.sprite.Group()
for i in range(14):
    brick = Brick(RED, 40, 20)
    brick.rect.x = 60 + i * 50
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(ORANGE, 40, 20)
    brick.rect.x = 60 + i * 50
    brick.rect.y = 90
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(YELLOW, 40, 20)
    brick.rect.x = 60 + i * 50
    brick.rect.y = 120
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(LIGHTGREEN, 40, 20)
    brick.rect.x = 60 + i * 50
    brick.rect.y = 150
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(14):
    brick = Brick(GREEN, 40, 20)
    brick.rect.x = 60 + i * 50
    brick.rect.y = 180
    all_sprites_list.add(brick)
    all_bricks.add(brick)

#add paddle to the list of Sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)


#loop carries on until user exits
carryOn = True
pause = False

#to control screen update speed
clock = pygame.time.Clock()


#--------------sound effects----------------#
sound = pygame.mixer
pdl = sound.Sound('Sounds/paddle.wav')
wal = sound.Sound('Sounds/wall.wav')
brk = sound.Sound('Sounds/brick.wav')
game_over = sound.Sound('Sounds/game_over.wav')
win = sound.Sound('Sounds/win.wav')
fal = sound.Sound('Sounds/fall.wav')

#loop
while carryOn:
    
    #main event
    for event in pygame.event.get(): #user update
        if event.type == pygame.QUIT:
            carryOn =False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                carryOn = False
            if event.key==pygame.K_0:
                sound.music.pause()
            elif event.key==pygame.K_1:
                sound.music.unpause()
                
        
        #PAUSE GAME ||
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            while True:
                sound.music.pause()
                font = pygame.font.Font(None, 74)
                text = font.render("PAUSED", 1, WHITE)
                screen.blit(text, (300, 300))
                pygame.display.flip()
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    sound.music.unpause()
                    break #PLAY ▷
    
    
    #move paddle with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(8)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(8)
    if keys[pygame.K_UP]:
        paddle.moveUp(5)    
    if keys[pygame.K_DOWN]:
        paddle.moveDown(5)
        
        
    
    #game logic
    all_sprites_list.update()
        
    #check ball bounces
    
    if ball.rect.x >= 790:
        wal.play()
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        wal.play()
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        fal.play()
        ball.velocity[1] = -ball.velocity[1]
        #loses life 
        lives -= 1
        if lives == 0:
            sound.music.stop()
            pygame.time.wait(100)
            game_over.play()
            #display game over message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(5000)
            
            #stop game
            carryOn = False
    if ball.rect.y < 40:
        wal.play()
        ball.velocity[1] = -ball.velocity[1]
   
    #detect ball-paddle collision
    if pygame.sprite.collide_mask(ball, paddle):
        pdl.play()
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()
        
    #check brick collision
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        brk.play()
        ball.bounce()
        score += 1
        brick.kill()
        
        if len(all_bricks)==0:
            sound.music.stop()
            pygame.time.wait(100)
            win.play()
            #display level complete for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            
            #stop the game
            carryOn = False
    
    #Drawing code
    #clear screen to dark blue
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0,38], [800,38], 2)
        
    #display score and lives
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
    
    #draaw all the Sprites in one go. currently 2 Sprites
    all_sprites_list.draw(screen)
    
    #update screen with drawing
    pygame.display.flip()
    
    #limit to 60 fps
    clock.tick(60)
    
#Once we have exited the main program loop we can stop the game engine
pygame.quit()