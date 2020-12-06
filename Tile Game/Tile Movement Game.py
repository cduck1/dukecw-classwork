import pygame
import random
import time
import os

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

current_path = os.path.dirname("__file__")#where this file is located
image_path = os.path.join(current_path, 'images')
BACKGROUND_IMAGE = pygame.image.load(os.path.join(image_path, 'dresize.png'))

# Set the screen width and height
size = (1200,1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tile Movement Game")

# Loop until the user clicks the close button
done = False

# CREATE GROUPS
# Create groups for each sprite
player_group = pygame.sprite.Group()
allwall_group = pygame.sprite.Group()   # All wall group is a group including all inner and outer walls
outerwall_group = pygame.sprite.Group()
innerwall_group = pygame.sprite.Group()
chest_group = pygame.sprite.Group()
sword_group = pygame.sprite.Group()
key_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
bulletleft_group = pygame.sprite.Group()
bulletright_group = pygame.sprite.Group()
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
        # Create a sprite and fill it with a the image
        self.image = pygame.image.load(os.path.join(image_path, "playersprite.png"))
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Set a speed vector
        self.change_x = 0
        self.change_y = 0
        # Variables
        self.health = 100
        self.points = 0
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

        # Did we HIT AN chest while moving left/right 
        chest_hit_group = pygame.sprite.spritecollide(self, chest_group, False)
        for chest in chest_hit_group:
            # If we are moving right, set our right side to the left side of the chest we hit
            if self.change_x > 0:
                self.rect.right = chest.rect.left
            else:
                # Otherwise if we are moving left, do the opposite
                self.rect.left = chest.rect.right

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

        # Did we HIT AN chest while moving up/down
        chest_hit_group = pygame.sprite.spritecollide(self, chest_group, False)
        for chest in chest_hit_group:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = chest.rect.top
            else:
                self.rect.top = chest.rect.bottom

        # Resets the speed change to 0 every update so that the speed doesn't accelerate infinitely
        self.change_x = 0
        self.change_y = 0

        # Instatiates the portal when keys = 4
        if self.keys == 4:
            myPortal = portal(PURPLE, 200, 200, 480, 360) # A 3x3 block portal spawns in the middle of the screen
            portal_group.add(myPortal)
            all_sprites_group.add(myPortal)
            self.keys = 0
            print("Portal has opened")

        # If the player's health reaches 0, kill the player and end the game
        if self.health <= 0:
            endgame()

    # Instantating the sword
    def spawnsword(self):
        # The sword is spawned on the right side of the player
        if sword.swordavaliable == True:
            mySword = sword(RED, 10, 4, self.rect.x + 40, self.rect.y + 18)
            sword_group.add(mySword)
            all_sprites_group.add(mySword)
            sword.swordavaliable = False

# Making the wall class
class outerwall(pygame.sprite.Sprite):
    # Define the constructor for the wall class
    def __init__(self, color, width, height, x, y):
        super().__init__()
        # Create a sprite and fill it with a the image
        self.image = pygame.image.load(os.path.join(image_path, "walltile2resize.jpg"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        # The right walls shoot bullets and the player must dodge them
        for self in outerwall_group:
            # If the wall is on the left side of the map, spawn a leftbullet that travels right
            if (random.randint(0,50000) == 1) and (self.rect.x == 0):
                myBulletLeft = bullet(RED, 15, 15, self.rect.x + 40, self.rect.y + 20)
                bulletleft_group.add(myBulletLeft)
                bullet_group.add(myBulletLeft)
                all_sprites_group.add(myBulletLeft)
                
class innerwall(outerwall):
    pass

# Making the chest class
class chest(pygame.sprite.Sprite):
    # Define the constructor for the chest
    def __init__(self, color, width, height, x_speed, y_speed, x, y):
        # Call the super class (the super class for the player is sprite)
        super().__init__()
        # Create a sprite and fill it with a the image
        self.image = pygame.image.load(os.path.join(image_path, "chestspriteresize.png"))
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Variables
        self.health = 100

    def update(self):
        # If the sword and the chest collide, minus health from the chest
        chest_hit_group = pygame.sprite.groupcollide(chest_group, sword_group, False, False)
        for self in chest_hit_group:
            self.health -= random.randint(1,3) # Makes the sword do a random amount of damage between 1 and 3 (such low damage so that the chest doesnt die instantly) - the damage done is minused off the chest's health. Need to use a data hiding method here (do self.health -= mySword.damage) but there is no mySword as it is a local variable - need a fix
            if self.health > 0:
                print("chest Health: " + str(self.health))
            else:
                print("chest is dead")
            
            # Remove the chest from the screen when it's health = 0 or less
            # When the chest dies, spawn a key on its position
            if self.health < 1:
                myKey = key(PINK, 20, 20, self.rect.x + 10, self.rect.y + 10)
                key_group.add(myKey)
                all_sprites_group.add(myKey)
                self.kill()

# Making the sword class
class sword(pygame.sprite.Sprite):
    # Define the constructor for the chest
    def __init__(self, color, width, height, x, y):
        # Call the super class (the super class for the player is sprite)
        super().__init__()
        # Create a sprite and fill it with the sword image
        self.image =  pygame.image.load(os.path.join(image_path,"swordresize.png"))
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Variables
        self.swordavaliable = True
        self.damage = random.randint(20,50) # Makes the sword do a random amount of damage between 20 and 60 - the damage done is minused off the chest's health - doesnt work because mychest doesn't exist

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
    # Define the constructor for the chest
    def __init__(self, color, width, height, x, y):
        # Call the super class (the super class for the player is sprite)
        super().__init__()
        # Create a sprite and fill it with a the image
        self.image = pygame.image.load(os.path.join(image_path, "keyresize.png"))
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
    # Define the constructor for the chest
    def __init__(self, color, width, height, x, y):
        # Call the super class (the super class for the player is sprite)
        super().__init__()
        # Create a sprite and fill it with a the image
        self.image = pygame.image.load(os.path.join(image_path, "netherportalresize.png"))
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    # When the player collides with the portal, new 4 new enemies are spawned in random places on the map, and the player gains 50 points
    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            self.kill()
            myPlayer.points += 50
            mychest = chest(YELLOW, 40, 40, 20, 20, 80, 80)
            chest_group.add(mychest)
            all_sprites_group.add(mychest)
            mychest = chest(YELLOW, 40, 40, 20, 20, 80, 880)
            chest_group.add(mychest)
            all_sprites_group.add(mychest)
            mychest = chest(YELLOW, 40, 40, 20, 20, 1080, 80)
            chest_group.add(mychest)
            all_sprites_group.add(mychest)
            mychest = chest(YELLOW, 40, 40, 20, 20, 1080, 880)
            chest_group.add(mychest)
            all_sprites_group.add(mychest)


class bullet(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, color, width, height, x, y):
        # Call the sprite constructor
        super().__init__()
        self.image = pygame.image.load(os.path.join(image_path, "bulletbillresize.png"))
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        # Makes the bullets travel right if they are bullets from the left walls and vice versa
        for self in bulletleft_group:
            self.rect.x += 1
        # If the bullet collides with the player, -20 health off the player and kill the bullet
        for self in bullet_group:
            if pygame.sprite.groupcollide(bullet_group, player_group, True, False):
                myPlayer.health -= 20
        # If the bullet hits any wall, including outer walls, kill it
        for self in bullet_group:
            if pygame.sprite.groupcollide(bullet_group, allwall_group, True, False):
                pass
        # If the bullet hits any chest, including outer walls, kill it
        for self in bullet_group:
            if pygame.sprite.groupcollide(bullet_group, chest_group, True, False):
                pass
        for self in bullet_group:
            if pygame.sprite.groupcollide(bullet_group, portal_group, True, False):
                pass
    
# When the player's health is 0 (or less), this is called and this wipes the screen and displays "GAME OVER"
def endgame():
    myPlayer.kill()
    for myBullet in bullet_group:
        myBullet.kill()
    for myWall in allwall_group:
        myWall.kill()
    for mychest in chest_group:
        mychest.kill()
    screen.fill(BLACK)
    # Draw "GAME OVER"
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render(("GAME OVER"), 1, WHITE)
    screen.blit(text, (500, 500))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

    
# Draw player attributes - health, money, keys
def displaytext():
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(("HEALTH: " + str(myPlayer.health)), 1, WHITE)
    screen.blit(text, (10, 15))

    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(("POINTS: " + str(myPlayer.points)), 1, WHITE)
    screen.blit(text, (10, 30))

    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(("KEYS: " + str(myPlayer.keys)), 1, WHITE)
    screen.blit(text, (10, 45))
    
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
# 4 = chest start point
level1 =   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
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
            1,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,1,
            1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


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
    if level1[i] == 1:
        myOuterWall = outerwall(RED, 40, 40, temp_x, temp_y)
        outerwall_group.add(myOuterWall)
        allwall_group.add(myOuterWall)
        all_sprites_group.add(myOuterWall)
    # 2s in the array represent inner walls
    if level1[i] == 2:
        myInnerWall = innerwall(RED, 40, 40, temp_x, temp_y)
        innerwall_group.add(myInnerWall)
        allwall_group.add(myInnerWall)
        all_sprites_group.add(myInnerWall)
    # 3s in the array represent the starting position of the player
    if level1[i] == 3:
        # Instantiate the player class - colour, width, height, x, y, speed
        myPlayer = player(BLUE, 40, 40, 20, 20, temp_x, temp_y)
        # Add the player to a player group and an all sprites group
        player_group.add(myPlayer)
        all_sprites_group.add(myPlayer)
    # 4s in the array represent the starting positions on the enemies
    if level1[i] == 4:
        mychest = chest(YELLOW, 40, 40, 20, 20, temp_x, temp_y)
        chest_group.add(mychest)
        all_sprites_group.add(mychest)

# MAIN PROGRAM LOOP
# Loop until the user clicks the close button.
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

    # Making the screen background black
    screen.fill(BLACK)
    # Draws the background image
    screen.blit(BACKGROUND_IMAGE, [0,0])
    # Draws all the sprites
    all_sprites_group.draw(screen)

    # Draw player attributes - health, money, keys
    displaytext()

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()