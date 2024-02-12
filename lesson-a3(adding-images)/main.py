import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaidors")
icon = pygame.image.load("./assets/images/ufo.png")
pygame.display.set_icon(icon)

# loading the player image
playerIcon = pygame.image.load("./assets/images/spaceship.png")
playerX = 370
playerY = 510

# resizing the player image
newW, newH = 60, 60
playerIcon = pygame.transform.scale(playerIcon, (newW, newH))

# creating our player entity
def player():
  # seting the image of the player entity
  screen.blit(playerIcon, (playerX, playerY))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((0, 0, 0))
  
  # adding the player entity to the screen
  player()
 
  pygame.display.update()