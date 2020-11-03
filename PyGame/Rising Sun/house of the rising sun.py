### SRC - Great, well done.
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
pygame.display.set_caption("House")
# -- Exit game flag set to false
done = False
sun_x = 40
sun_y = 100
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- Game Loop
while not done:
  # -- User input and controls
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    #End If
  #Next event
  # -- Game logic goes after this comment
  sun_x = sun_x + 5
  # -- Screen background is BLACK
  screen.fill (BLACK)
  # -- Draw here
  pygame.draw.rect(screen, BLUE, (220, 165, 200, 150))
  pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), 40, 0)
  # -- flip display to reveal new position of objects
  pygame.display.flip()
  # - The clock ticks over
  clock.tick(60)
pygame.quit()
