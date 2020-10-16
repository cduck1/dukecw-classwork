import pygame
import random
import math

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Invader")
score = 0
lives = 3
print("Lives: " + str(lives))
# Create a list of the invader blocks
invader_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
deathbarrier_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
# -- Define the class invader which is a sprite
class invader(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, color, width, height, speed, x, y):
        # Set the speed of the sprite
        self.speed = speed
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
    #End Procedure
    def update(self):
        self.rect.y = self.rect.y + self.speed
#End Class

# -- Define the class player which is a sprite
class player(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, color, width, height):
        # Set the speed of the sprite
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 460
        self.speed = 1
        #End Procedure
    def update(self):
        if self.rect.x > 630:
            self.rect.x = 630
        elif self.rect.x < 0:
            self.rect.x = 0
    def moveRight(self, speed):
        self.rect.x += speed
    #End Procedure
    def moveLeft(self, speed):
        self.rect.x -= speed
    #End Procedure 
#End Class

class bullet(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, color, width, height, x, y):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        #End Procedure
    def update(self):
        self.rect.y -= 3            
    #End Procedure
#End Class

class deathBarrier(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        #start of the death barrier is at at the bottom left of the screen 
        self.rect.y = 480
        self.rect.x = 0

def gameLoop(lives, score):
    # -- Exit game flag set to false
    done = False
    # -- Variables
    bullet_count = 100
    
    #end the game when the player's lives are 0
    if lives == 0:
        print("NO LIVES. GAME OVER.")
        done = True

    # Create the invaderships
    number_of_ships = 10 # we are creating 50 invaders
    for x in range (number_of_ships):
        my_invader = invader(BLUE, 10, 10, 1, random.randrange(0, 600), random.randrange(-50, 0)) # invaderships are white with size 5 by 5 px
        invader_group.add(my_invader) # adds the new invadership to the group of invaderships
        all_sprites_group.add(my_invader) # adds it to the group of all Sprites
    #Next
                
    # Create the player
    my_player = player(YELLOW, 10, 10)
    player_group.add(my_player)
    all_sprites_group.add(my_player)

    # create the death barrier
    my_deathbarrier = deathBarrier(RED, 640, 1)
    deathbarrier_group.add(my_deathbarrier)
    all_sprites_group.add(my_deathbarrier)

    # -- Game Loop
    while not done:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN: # - a key is down
                if event.key == pygame.K_ESCAPE: # - if the escape key pressed
                    done = True
                #End If
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            # Create the bullet
            my_bullet = bullet(RED, 2, 2, (my_player.rect.x) + 4, my_player.rect.y)
            bullet_group.add(my_bullet)
            all_sprites_group.add(my_bullet)
            bullet_count = bullet_count - 1
            print("Bullet count: " + str(bullet_count))
        if keys[pygame.K_LEFT]:
            my_player.moveLeft(3)
        if keys[pygame.K_RIGHT]:
            my_player.moveRight(3)
                        
        # -- Game logic goes after this comment
        all_sprites_group.update()
        # -- when invader hits the player add 5 to score.
        player_hit_group = pygame.sprite.spritecollide(my_player, invader_group, True)
        # -- when invader hits the bullet add 5 to score.
        for my_bullet in bullet_group:
            if pygame.sprite.groupcollide(bullet_group, invader_group, True, True):
                score = score + 5
                print("Score: " + str(score))

        if pygame.sprite.spritecollide(my_deathbarrier, invader_group, False):
            lives = lives - 1
            print("Lives: " + str(lives))
            for my_invader in invader_group:
                my_invader.rect.y = random.randrange(-50, 0)
            my_player.kill()
            gameLoop(lives, score)
            
        # -- Screen background is BLACK
        screen.fill (BLACK)
        # -- Draw here
        all_sprites_group.draw(screen)
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
        #End While - End of game loop
gameLoop(lives, score)
pygame.quit()
