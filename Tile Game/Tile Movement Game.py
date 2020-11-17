import pygame

# Defining Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

pygame.init()

# Set the screen width and height
size = (1000,1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tile Movement Game")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# CLASSES
# Making the player class
class player(pygame.sprite.Sprite):
    # Define the constructor for the invader
    def __init__(self, myColor, myWidth, myHeight, myX, myY, mySpeed):
        # Call the super class (the super class for the player is sprite)
        super().__init__()
        # Create a sprite and fill it with a colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.speed = 1

# MAIN PROGRAM LOOP
while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Game logic should go here
 
    # Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # Making the screen background black
    screen.fill(BLACK)
 
    # Drawing code should go here
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()