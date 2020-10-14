import pygame 
# -- Global Constants 
# -- Colours 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
BLUE = (50, 50, 255) 
YELLOW = (255, 255, 0) 
# -- Initialise PyGame 
pygame.init() 
# -- Blank Screen 
size = (640, 480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("Pong") 
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock() 
# -- Game Loop 
def gameloop():
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
    y_padd = 20 
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
        if event.type == pygame.KEYDOWN:
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
        if x_val < 15 and y_val > y_padd and y_val < y_padd + 60:
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
        font = pygame.font.Font(None, 45)
        text = font.render("Score: " + str(score), 1, WHITE)
        screen.blit(text, (310, 40))
                            
        # -- display lives
        font = pygame.font.Font(None, 45)
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (310, 10))
        
        # -- getting the game to end when lives = 0
        if lives == 0:
            done = True
            gameover()  
    
        # -- flip display to reveal new position of objects 
        pygame.display.flip() 
    
        # - The clock ticks over 
        clock.tick(60)
        
# -- getting the game to end when lives = 0
def gameover():
    screen.fill(BLACK)
    font = pygame.font.Font("freesansbold.ttf", 50)
    text = font.render("GAME OVER", 1, WHITE)
    screen.blit(text, (310, 10))
    pygame.display.flip()
    clock.tick(60)
        
gameloop()        
pygame.quit()
