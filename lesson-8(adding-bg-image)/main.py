import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaidors")
icon = pygame.image.load("./assets/images/ufo.png")
pygame.display.set_icon(icon) 

playerImage = pygame.image.load("./assets/images/spaceship.png")
playerX, playerY = 370, 510
speedPlayerX, playerX_moving =.5, 0
newPlayerW, newPlayerH = 60, 60
playerImage = pygame.transform.scale(playerImage, (newPlayerW, newPlayerH))

enemyImage = pygame.image.load("./assets/images/enemy.png")
enemyX, enemyY = random.randint(0, 750), random.randint(30, 100)
enemyX_moving, enemyY_moving = .3, 40
newEnemyW, newEnemyH = 50, 50
enemyImage = pygame.transform.scale(enemyImage, (newEnemyW, newEnemyH))

# set the image
bg_image = pygame.image.load("./assets/images/bg-image.jpg")
bg_image = pygame.transform.scale(bg_image, (800, 600))
leftBoundary = 0
rightBoundary = 740

def player(x, y):
  screen.blit(playerImage, (x, y))


def enemy(x, y):
  screen.blit(enemyImage, (x, y))

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

  enemyX += enemyX_moving
  if enemyX > rightBoundary or enemyX < leftBoundary:
    enemyX_moving *= -1
    enemyY += enemyY_moving

  # add the image
  # screen.fill((0, 0, 0))
  screen.blit(bg_image, (0, 0))

  player(playerX, playerY)

  enemy(enemyX, enemyY)
 
  pygame.display.update()