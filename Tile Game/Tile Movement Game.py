import pygame
import random

# Defining Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PINK = (255,20,147)
PURPLE = (138,43,226)

pygame.init()

# Set the screen width and height
size = (1200,1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tile Movement Game")

# Loop until the user clicks the close button.
done = False

# CREATE GROUPS
# Create groups for each sprite
player_group = pygame.sprite.Group()
allwall_group = pygame.sprite.Group()   # All wall group is a group including all inner and outer walls
outerwall_group = pygame.sprite.Group()
innerwall_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
sword_group = pygame.sprite.Group()
key_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()
# Create a group of all sprites together
all_sprites_group = pygame.sprite.Group()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# CLASSES
# Making the player class
class player(pygame.sprite.Sprite):
    # Define the constructor for the player
    def __init__(self, color, width, height, x_speed, y_speed, x, y):
        # Call the super class (the super class for the player is sprite)
        super().__init__()
        # Create a sprite and fill it with a colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Set a speed vector
        self.change_x = 0
        self.change_y = 0
        # Variables
        self.health = 300
        self.money = 0
        self.keys = 0
 
    # Change the x and y speed of the player
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    # This update function moves the player and checks whether the player has collided with a wall - if it does it stops
    def update(self):
        # Move the player left/right
        self.rect.x += self.change_x
        # Did we HIT A WALL while moving left/right
        wall_hit_group = pygame.sprite.spritecollide(self, allwall_group, False)
        for wall in wall_hit_group:
            # If we are moving right, set our right side to the left side of the wall we hit
            if self.change_x > 0:
                self.rect.right = wall.rect.left
            else:
                # Otherwise if we are moving left, do the opposite
                self.rect.left = wall.rect.right

        # Did we HIT AN ENEMY while moving left/right 
        enemy_hit_group = pygame.sprite.spritecollide(self, enemy_group, False)
        for enemy in enemy_hit_group:
            # If we are moving right, set our right side to the left side of the enemy we hit
            if self.change_x > 0:
                self.rect.right = enemy.rect.left
            else:
                # Otherwise if we are moving left, do the opposite
                self.rect.left = enemy.rect.right

        # Move the player up/down
        self.rect.y += self.change_y
        # Did we hit a WALL while moving up/down
        wall_hit_group = pygame.sprite.spritecollide(self, allwall_group, False)
        for wall in wall_hit_group:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom

        # Did we HIT AN ENEMY while moving up/down
        enemy_hit_group = pygame.sprite.spritecollide(self, enemy_group, False)
        for enemy in enemy_hit_group:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = enemy.rect.top
            else:
                self.rect.top = enemy.rect.bottom

        # Resets the speed change to 0 every update so that the speed doesn't accelerate infinitely
        self.change_x = 0
        self.change_y = 0

        # Calls the makeportal() method when keys = 3
        if self.keys == 3:
            myPlayer.makeportal()
            changelevel()

    # Instantating the sword
    def spawnsword(self):
        # The sword is spawned on the right side of the player
        if sword.swordavaliable == True:
            mySword = sword(RED, 10, 4, self.rect.x + 40, self.rect.y + 18)
            sword_group.add(mySword)
            all_sprites_group.add(mySword)
            sword.swordavaliable = False

    def makeportal(self):
        # Instantiates the portal
        myPortal = portal(PURPLE, 200, 200, 480, 360) # A 3x3 block portal spawns in the middle of the screen
        portal_group.add(myPortal)
        all_sprites_group.add(myPortal)

# Making the wall class
class outerwall(pygame.sprite.Sprite):
    # Define the constructor for the wall class
    def __init__(self, color, width, height, x, y):
        super().__init__()
        # Create a sprite an fill it with the colour with x and y values
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class innerwall(outerwall):
    pass

# Making the enemy class
class enemy(pygame.sprite.Sprite):
    # Define the constructor for the enemy
    def __init__(self, color, width, height, x_speed, y_speed, x, y):
        # Call the super class (the super class for the player is sprite)
        super().__init__()
        # Create a sprite and fill it with a colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Variables
        self.health = 100

    def update(self):
        # If the sword and the enemy collide, minus health from the enemy
        enemy_hit_group = pygame.sprite.groupcollide(enemy_group, sword_group, False, False)
        for self in enemy_hit_group:
            self.health -= random.randint(1,3) # Makes the sword do a random amount of damage between 1 and 3 (such low damage so that the enemy doesnt die instantly)- the damage done is minused off the enemy's health. Need to use a data hiding method here (do self.health -= mySword.damage) but there is no mySword as it is a local variable - need a fix
            if self.health > 0:
                print("Enemy Health: " + str(self.health))
            else:
                print("Enemy is dead")
            
            # Remove the enemy from the screen when it's health = 0 or less
            # When the enemy dies, spawn a key on its position
            if self.health < 1:
                myKey = key(PINK, 20, 20, self.rect.x + 10, self.rect.y + 10)
                key_group.add(myKey)
                all_sprites_group.add(myKey)
                self.kill()

# Making the sword class
class sword(pygame.sprite.Sprite):
    # Define the constructor for the enemy
    def __init__(self, color, width, height, x, y):
        # Call the super class (the super class for the player is sprite)
        super().__init__()
        # Create a sprite and fill it with a colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Variables
        self.swordavaliable = True
        self.damage = random.randint(20,50) # Makes the sword do a random amount of damage between 20 and 60 - the damage done is minused off the enemy's health - doesnt work because myEnemy doesn't exist

    def update(self):
        # While SPACE is being held down, keep the sword in the same position (attached to the right side of the player). If space is not being held down, delete the sword
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.rect.x = myPlayer.rect.x + 40
            self.rect.y = myPlayer.rect.y + 18
        else:
            self.kill()

# Making the keys class
class key(pygame.sprite.Sprite):
    # Define the constructor for the enemy
    def __init__(self, color, width, height, x, y):
        # Call the super class (the super class for the player is sprite)
        super().__init__()
        # Create a sprite and fill it with a colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # If the player and the key collides, add 1 key to myPlayer.keys
        if pygame.sprite.groupcollide(key_group, player_group, True, False):
            myPlayer.keys += 1

# Making a portal class - takes the player to the next level
class portal(pygame.sprite.Sprite):
    # Define the constructor for the enemy
    def __init__(self, color, width, height, x, y):
        # Call the super class (the super class for the player is sprite)
        super().__init__()
        # Create a sprite and fill it with a colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def changelevel(temp_level):
    temp_level = level[i+1]

# INSTANTATION CODE


# CREATING THE LAYOUT OF THE GAME USING A LIST 
# Plan for creating the walls: have a list of 625 items, create wall at a specific x and y coordinates if there is a 1; once you get to the 25th element (to the end of the screen), go you down 40 pixels and start at x coord 0
# Rows are sets of 30 elements
# There are 750 total elements because each element represent a block of 40 by 40 and 25 x 30 = 750
# Top and bottom walls (30 1s) = 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
# Side walls = 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
# 0 = nothing present
# 1 = outer wall present
# 2 = inner wall present
# 3 = player start point
# 4 = enemy start point
level1 =   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

level2 =   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# Creating SEVERAL LEVEL
levels = [level1, level2]

# temp_level is the current level that the player is playing
temp_level = levels[0]

for i in range (0,750):
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
    elif i % 30 == 0:
        temp_x = 0
        temp_y = temp_y + 40
    # 1s in the array represent outer walls
    if temp_level[i] == 1:
        myOuterWall = outerwall(RED, 40, 40, temp_x, temp_y)
        outerwall_group.add(myOuterWall)
        allwall_group.add(myOuterWall)
        all_sprites_group.add(myOuterWall)
    # 2s in the array represent inner walls
    if temp_level[i] == 2:
        myInnerWall = innerwall(RED, 40, 40, temp_x, temp_y)
        innerwall_group.add(myInnerWall)
        allwall_group.add(myInnerWall)
        all_sprites_group.add(myInnerWall)
    # 3s in the array represent the starting position of the player
    if temp_level[i] == 3:
        # Instantiate the player class - colour, width, height, x, y, speed
        myPlayer = player(BLUE, 40, 40, 20, 20, temp_x, temp_y)
        # Add the player to a player group and an all sprites group
        player_group.add(myPlayer)
        all_sprites_group.add(myPlayer)
    # 4s in the array represent the starting positions on the enemies
    if temp_level[i] == 4:
        myEnemy = enemy(YELLOW, 40, 40, 20, 20, temp_x, temp_y)
        enemy_group.add(myEnemy)
        all_sprites_group.add(myEnemy)


# MAIN PROGRAM LOOP
while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        myPlayer.changespeed(-7, 0)
    if keys[pygame.K_RIGHT]:
        myPlayer.changespeed(7, 0)
    if keys[pygame.K_UP]:
        myPlayer.changespeed(0, -7)
    if keys[pygame.K_DOWN]:
        myPlayer.changespeed(0, 7)
    if keys[pygame.K_SPACE]:
        myPlayer.spawnsword()
    else:
        sword.swordavaliable = True # A new sword can only be made while the player isn't holding down SPACE - otherwise infinite swords are created but they are all on top of each other


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

    # Draw player attributes - health, money, keys
    font = pygame.font.Font('freesansbold.ttf', 17)
    text = font.render(("HEALTH: " + str(myPlayer.health)), 1, WHITE)
    screen.blit(text, (5, 5))

    font = pygame.font.Font('freesansbold.ttf', 17)
    text = font.render(("MONEY: " + str(myPlayer.money)), 1, WHITE)
    screen.blit(text, (5, 20))

    font = pygame.font.Font('freesansbold.ttf', 17)
    text = font.render(("KEYS: " + str(myPlayer.keys)), 1, WHITE)
    screen.blit(text, (5, 35))

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()