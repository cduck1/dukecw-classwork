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

# CREATE GROUPS
# Create groups for each sprite
player_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
# Create a group of all sprites together
all_sprites_group = pygame.sprite.Group()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# CLASSES
# Making the player class
class player(pygame.sprite.Sprite):
    # Define the constructor for the player
    def __init__(self, color, width, height, x_speed, y_speed):
        # Call the super class (the super class for the player is sprite)
        super().__init__()
        # Create a sprite and fill it with a colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        # Change the speed of the player
        self.change_x += x
        self.change_y += y
 
    def update(self):
        # Update the player position

        # Move left/right
        self.rect.x += self.change_x
        # Check to see if this update causes us to hit a wall
        wall_hit_group = pygame.sprite.spritecollide(self, wall_group, False)
        for wall in wall_hit_group:
            # If we are moving right, set our right side to the left side of the wall we hit
            if self.change_x > 0:
                self.rect.right = wall.rect.left
            else:
                # Otherwise if we are moving left, do the opposite
                self.rect.left = wall.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
        # Check and see if we hit anything
        wall_hit_group = pygame.sprite.spritecollide(self, wall_group, False)
        for wall in wall_hit_group:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom
        
        # Resets the change to 0 every update so that the speed doesn't accelerate infinitely
        self.change_x = 0
        self.change_y = 0

    # Procedure for what happens when the right and left arrow key is pressed
    def moveRight(self, x_speed):
        self.rect.x += x_speed
    def moveLeft(self, x_speed):
        self.rect.x -= x_speed
    def moveUp(self, y_speed):
        self.rect.y -= y_speed
    def moveDown(self, y_speed):
            self.rect.y += y_speed

# Making the wall class
class wall(pygame.sprite.Sprite):
    # Define the constructor for the wall class
    def __init__(self, color, width, height, x, y):
        super().__init__()
        # Create a sprite an fill it with the colour with x and y values
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# INSTANTATION CODE
# Instantiate the player class - colour, width, height, x, y, speed
myPlayer = player(BLUE, 40, 40, 20, 20)
# Add the player to a player group and an all sprites group
player_group.add(myPlayer)
all_sprites_group.add(myPlayer)

# CREATING THE WALLS USING A LIST 
# Plan for creating the walls: have a list of 625 items, create wall at a specific x and y coordinates if there is a 1; once you get to the 25th element (to the end of the screen), go you down 40 pixels and start at x coord 0
# Rows are sets of 25 elements
# There are 625 total elements because each element represent a block of 40 by 40 and 25 x 25 = 625
# Top and bottom walls (25 1s) = 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
# Side walls = 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
wall_present = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
for i in range (0,625):
    # temp_x and temp_y are the temporary values where the wall will be created for that iteration of the for loop, so if there is a 1 at that position, it will be created at a different x and y each time
    # We have an if i == 0 here because we need the walls to start at zero, if it didnt we would start with temp_x = temp_x + 40 and so fourth
    # Add 40 to the x coordinate for the wall when there is a y in the list
    if i == 0:
        temp_x = 0
    else:
        temp_x = temp_x + 40
    
    # Increases the y value (goes down to the next row of walls) once the row is filled (after 25 elements in the list), but dont change it when i = 0
    if i == 0:
        temp_y = 0
    elif i % 25 == 0:
        temp_x = 0
        temp_y = temp_y + 40
        
    if wall_present[i] == 1:
        myWall = wall(RED, 40, 40, temp_x, temp_y)
        wall_group.add(myWall)
        all_sprites_group.add(myWall)


# MAIN PROGRAM LOOP
while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        myPlayer.changespeed(-20, 0)
    if keys[pygame.K_RIGHT]:
        myPlayer.changespeed(20, 0)
    if keys[pygame.K_UP]:
        myPlayer.changespeed(0, -20)
    if keys[pygame.K_DOWN]:
        myPlayer.changespeed(0, 20)
 
    # Game logic should go here
    all_sprites_group.update()

    # Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # Making the screen background black
    screen.fill(BLACK)

    # Draws all the sprites
    all_sprites_group.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()