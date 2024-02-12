import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaidors")
icon = pygame.image.load("./assets/images/ufo.png")
pygame.display.set_icon(icon)

playerImage = pygame.image.load("./assets/images/spaceship.png")
playerX, playerY, speedPlayerX, playerX_moving = 370, 510, .5, 0
newPlayerW, newPlayerH = 60, 60
playerImage = pygame.transform.scale(playerImage, (newPlayerW, newPlayerH))

# bring in the enemy image and sent the size and location of it
enemyImage = pygame.image.load("./assets/images/enemy.png")
enemyX, enemyY = random.randint(0, 750), random.randint(30, 100)
newEnemyW, newEnemyH = 50, 50
enemyImage = pygame.transform.scale(enemyImage, (newEnemyW, newEnemyH))

leftBoundary = 0
rightBoundary = 740

# create the enemy entity
def enemy(x, y):
  # set the enemy image
  screen.blit(enemyImage, (x, y))

def player(x, y):
  screen.blit(playerImage, (x, y))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN: 
      if event.key == pygame.K_LEFT:
        playerX_moving = -speedPlayerX
      elif event.key == pygame.K_RIGHT:
        playerX_moving = speedPlayerX
    elif event.type == pygame.KEYUP: 
      playerX_moving = 0
        
  if (playerX_moving == -speedPlayerX and playerX > leftBoundary) or (playerX_moving == speedPlayerX and playerX < rightBoundary):
    playerX += playerX_moving

  screen.fill((0, 0, 0))

  player(playerX, playerY)

  # add the enemy entity to the screen
  enemy(enemyX, enemyY)
 
  pygame.display.update()