import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaidors")
icon = pygame.image.load("./assets/images/ufo.png")
pygame.display.set_icon(icon)

playerIcon = pygame.image.load("./assets/images/spaceship.png")
playerX = 370
playerY = 510

newW, newH = 60, 60
playerIcon = pygame.transform.scale(playerIcon, (newW, newH))

# adding the x and y parameters
def player(x, y):
  screen.blit(playerIcon, (x, y))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # how to implement movement functionality
  # playerX += .1 # move right
  # playerX -= .1 # move left
  # playerY += .1 # move up
  # playerY -= .1 # move down

  screen.fill((0, 0, 0))

  player(playerX, playerY)
 
  pygame.display.update()