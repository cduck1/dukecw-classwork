### SRC - This is an excellent effort at this stage. There is still much to
### learn to improve your code, as you should try and only write code once if you can.

import pygame
import time
# -- Global Constants 
# -- Colours 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
BLUE = (50, 50, 255) 
YELLOW = (255, 255, 0)
GREY = (180, 180, 180)
# -- Initialise PyGame 
pygame.init() 
# -- Blank Screen 
size = (640, 480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("Pong") 
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock() 

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                intro = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE: 
                    intro=False                      
        # -- Drawing the menu screen
        screen.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 84)
        text = font.render(str("PONG"), 1, WHITE)
        text_rect = text.get_rect(center=(320, 80))
        screen.blit(text, text_rect)

        button_1("SINGLEPLAYER",200,250,250,60,WHITE,GREY,"1")
        button_1("VS AI",200,330,250,60,WHITE,GREY,"2")
        button_1("QUIT",200,410,250,60,WHITE,GREY,"Q")
            
        pygame.display.flip()
        clock.tick(60)

def text_objects(text,font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def singleplayer_gameloop():
    # -- Exit game flag set to false 
    done = False 
    # -- Variables 
    # ---- top_left_screen = (0, 0) 
    # ---- top_right_screen = (640, 0) 
    # ---- bottom_left_screen = (0, 480) 
    # ---- bottom_right_screen = (640, 480)
    padd_width = 15 
    padd_length = 60 
    x_padd = 0 
    y_padd = 210 
    x_val = 150 
    y_val = 200 
    ball_width = 20 
    x_offset = -1
    y_offset = 1
    lives = 3
    score = 0
    
    while not done:
        # -- User input and controls 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y_padd = y_padd - 5
        if keys[pygame.K_DOWN]:
            y_padd = y_padd + 5
            
        # -- Game logic goes after this comment
        # -- The paddle can't go off the top or bottom
        if y_padd <= 0:
            y_padd = 0
            
        if y_padd >= 420:
            y_padd = 420

        # -- Getting the score to increase by 1 when the ball goes off the left edge
        if x_val == 0:
            lives = lives - 1
            x_val = 150
            y_val = 200
            
        # -- getting the right edge to bounce
        if x_val >= 620:
            x_val = 620
            x_offset = -x_offset
            
        # -- getting the top edge to bounce
        if y_val <= 0:
            y_val = 0
            y_offset = -y_offset
            
        # -- getting the bottom edge to bounce
        if y_val >= 460:
            y_val =  460
            y_offset = -y_offset
               
        # -- Check the criteria for hitting the paddle and getting the ball speed to increase with a score variable
        if x_val < 15 and y_val >= y_padd and y_val <= y_padd + 60:
            x_offset = x_offset * -1
            score = score + 1
            x_offset += 1
            y_offset += 1
            
        x_val = x_val + x_offset 
        y_val = y_val + y_offset
            
        # -- Screen background is BLACK 
        screen.fill(BLACK)
        
        # -- Draw here
        pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width)) 
        pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_width, padd_length))

        # -- display score (glitches when the ball goes off the left of the screen
        font = pygame.font.Font(None, 30)
        text = font.render("Score: " + str(score), 1, WHITE)
        screen.blit(text, (10, 30))
                            
        # -- display lives
        font = pygame.font.Font(None, 30)
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (10, 10))
        
        # -- getting the game to end when lives = 0
        if lives == 0:
            you_lose()
            done = True
    
        # -- flip display to reveal new position of objects 
        pygame.display.flip() 
    
        # - The clock ticks over 
        clock.tick(60)

# -- Game Loop 
def ai_gameloop():
    # -- Exit game flag set to false 
    done = False 
    # -- Variables 
    # ---- top_left_screen = (0, 0) 
    # ---- top_right_screen = (640, 0) 
    # ---- bottom_left_screen = (0, 480) 
    # ---- bottom_right_screen = (640, 480)
    ai_padd_width = 15
    ai_padd_length = 60
    ai_x_padd = 625
    ai_y_padd = 210
    padd_width = 15 
    padd_length = 60 
    x_padd = 0 
    y_padd = 210 
    x_val = 150 
    y_val = 200 
    ball_width = 20 
    x_offset = -1
    y_offset = 1
    lives = 3
    ai_lives = 3
    score = 0
    while not done:
        # -- User input and controls 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y_padd = y_padd - 5
        if keys[pygame.K_DOWN]:
            y_padd = y_padd + 5
            
        # -- Game logic goes after this comment
        # -- The paddles can't go off the top or bottom
        if y_padd <= 0:
            y_padd = 0
            
        if y_padd >= 420:
            y_padd = 420

        if ai_y_padd <= 0:
            ai_y_padd = 0
            
        if ai_y_padd >= 420:
            ai_y_padd = 420

        # -- Getting the score to increase by 1 when the ball goes off the left edge
        if x_val <= 0:
            lives = lives - 1
            x_val = 150
            y_val = 200
            y_padd = 210
            ai_y_padd = 210
            x_offset = -1
            y_offset = 1
            time.sleep(1)

        # -- getting the right edge to reset the ball and -1 from ai_lives
        if x_val >= 640:
            ai_lives = ai_lives - 1
            x_val = 150
            y_val = 200
            y_padd = 210
            ai_y_padd = 210
            x_offset = -1
            y_offset = 1
            time.sleep(1)

        # -- getting the top edge to bounce
        if y_val <= 0:
            y_val = 0
            y_offset = -y_offset
            
        # -- getting the bottom edge to bounce
        if y_val >= 460:
            y_val =  460
            y_offset = -y_offset
               
        # -- Check the criteria for hitting the paddle and getting the ball speed to increase with a score variable
        if x_val < 15 and y_val >= y_padd and y_val <= y_padd + 60:
            x_offset = x_offset * -1
            x_offset += 1
            y_offset += 1
            
        x_val = x_val + x_offset 
        y_val = y_val + y_offset

        # -- getting the ball to bounce off the ai_paddle
        if x_val > 605 and y_val >= ai_y_padd and y_val <= ai_y_padd + 60:
            x_offset = x_offset * -1
        
        # -- getting the ai to track the ball
        if ai_y_padd < y_val:
            ai_y_padd = ai_y_padd + 2
        elif ai_y_padd > y_val:
            ai_y_padd = ai_y_padd - 2
            
        # -- Screen background is BLACK 
        screen.fill(BLACK)
        
        # -- Draw here
        pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width)) 
        pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_width, padd_length))
        pygame.draw.rect(screen, YELLOW, (ai_x_padd, ai_y_padd, ai_padd_width, ai_padd_length))

        # -- display ai_lives
        font = pygame.font.Font(None, 30)
        text = font.render("Lives: " + str(ai_lives), 1, WHITE)
        screen.blit(text, (550, 10))
                            
        # -- display lives
        font = pygame.font.Font(None, 30)
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (10, 10))
        
        # -- getting the game to end when lives = 0
        if lives == 0:
            you_lose()
            done = True

        # -- getting the game to end when ai_lives = 0
        if ai_lives == 0:
            you_win()
            done = True
    
        # -- flip display to reveal new position of objects 
        pygame.display.flip() 
    
        # - The clock ticks over 
        clock.tick(60)


def button_1(msg1,xb1,yb1,wb1,hb1,icb1,acb1,action1=None): #msg1 = the message inside the button, xb1 = x coords of button, yb1 = y coords, wb1 = width, hb1 = height, icb1 = inactive colour, acb1 = active colour, action = the output when button is pressed
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if xb1+wb1 >mouse[0] > xb1 and yb1+hb1 > mouse[1] > yb1:
        pygame.draw.rect(screen, icb1,(xb1,yb1,wb1,hb1),5)
        if click[0] == 1 and action1 !=None:
            if action1 == "1":
                singleplayer_gameloop()
            elif action1 == "2":
                ai_gameloop()
            elif action1 == "Q":
                    pygame.quit()
    else:
        pygame.draw.rect(screen, acb1,(xb1,yb1,wb1,hb1),5)
        
    smallText = pygame.font.Font("freesansbold.ttf",30)
    textSurf, textRect = text_objects(msg1, smallText)
    textRect.center = ( (xb1+(wb1/2)), (yb1+(hb1/2)) )
    screen.blit(textSurf, textRect)
    
# -- getting the game to end when lives = 0
def you_lose():
    screen.fill(BLACK)
    font = pygame.font.Font("freesansbold.ttf", 50)
    text = font.render("YOU LOSE!", 1, WHITE)
    screen.blit(text, (300, 10))
    time.sleep(3)
    clock.tick(60)

# -- getting the game to end when lives = 0
def you_win():
    screen.fill(BLACK)
    font = pygame.font.Font("freesansbold.ttf", 50)
    text = font.render("YOU WIN!", 1, WHITE)
    screen.blit(text, (300, 10))
    time.sleep(3)
    clock.tick(60)
        
game_intro()       
pygame.quit()

