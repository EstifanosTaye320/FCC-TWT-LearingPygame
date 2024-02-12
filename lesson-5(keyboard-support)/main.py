import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaidors")
icon = pygame.image.load("./assets/images/ufo.png")
pygame.display.set_icon(icon)

playerIcon = pygame.image.load("./assets/images/spaceship.png")

# Declaring speed of change in the X direction
playerX, playerY, speedX, playerX_moving = 370, 510, .5, 0

newW, newH = 60, 60
playerIcon = pygame.transform.scale(playerIcon, (newW, newH))

# Boundaries
leftBoundary = -30
rightBoundary = 770

def player(x, y):
  screen.blit(playerIcon, (x, y))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN: 

      # Listen for key press and activate movment
      if event.key == pygame.K_LEFT:
        playerX_moving = -speedX
      elif event.key == pygame.K_RIGHT:
        playerX_moving = speedX
    elif event.type == pygame.KEYUP: 

      # Listen for key release and diactivate movment
      playerX_moving = 0
        
  # handle events active or inactive
  if (playerX_moving == -speedX and playerX > leftBoundary) or (playerX_moving == speedX and playerX < rightBoundary):
    playerX += playerX_moving

  screen.fill((0, 0, 0))

  player(playerX, playerY)
 
  pygame.display.update()