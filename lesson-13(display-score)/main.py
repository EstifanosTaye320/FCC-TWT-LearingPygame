import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaidors")
icon = pygame.image.load("./assets/images/ufo.png")
pygame.display.set_icon(icon) 

bg_image = pygame.image.load("./assets/images/bg-image.jpg")
bg_image = pygame.transform.scale(bg_image, (800, 600))
leftBoundary = 0
rightPlayerBoundary, rightEnemyBoundary = 740, 750
upperBoundary = 0

playerImage = pygame.image.load("./assets/images/spaceship.png")
playerX, playerY = 370, 510
speedPlayerX, playerX_moving =.5, 0
newPlayerW, newPlayerH = 60, 60
playerImage = pygame.transform.scale(playerImage, (newPlayerW, newPlayerH))

enemyX, enemyY = [], []
enemyX_moving= []
enemyImage = pygame.image.load("./assets/images/enemy.png")
newEnemyW, newEnemyH = 50, 50
enemyImage = pygame.transform.scale(enemyImage, (newEnemyW, newEnemyH))
enemyY_moving = 40

num_of_enemies = 6
for i in range(num_of_enemies):
  enemyX.append(random.randint(leftBoundary, rightEnemyBoundary-1))
  enemyY.append(random.randint(40, 100))
  enemyX_moving.append(.3)


bulletImage = pygame.image.load("./assets/images/bullet.png")
bulletX, bulletY = playerX , playerY
bulletY_moving = -1
newBulletW, newBulletH = 30, 30
bulletImage = pygame.transform.scale(bulletImage, (newBulletW, newBulletH))
bulletState = "ready"

# declaration of the font and font size
score = 0
font = pygame.font.Font("./assets/fonts/flamouse/Flamouse Personal Use Only.ttf",30)
textX, textY = 10, 10

def player(x, y):
  screen.blit(playerImage, (x, y))

def enemy(x, y):
  screen.blit(enemyImage, (x, y))

def Bullet(x, y):
  screen.blit(bulletImage, (x + 15, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
  distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
  if distance < 30:
    return True
  return False

def increaseSpeed(score):
  if score % 10 == 0 and score != 0:
    for i in range(len(enemyX_moving)):
      if enemyX_moving[i] < 0:
        enemyX_moving[i] -= .1
      else:
        enemyX_moving[i] += .1

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
      elif event.key == pygame.K_SPACE and bulletState is "ready":
        bulletX = playerX
        bulletState = "fire"
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerX_moving = 0
        
  if (playerX_moving == -speedPlayerX and playerX > leftBoundary) or (playerX_moving == speedPlayerX and playerX < rightPlayerBoundary):
    playerX += playerX_moving

  # initation of the score text (put on surface)
  text = font.render(f"Score: {score}", True, (255, 255, 255))

  screen.blit(bg_image, (0, 0))

  for i in range(num_of_enemies):
    enemyX[i] += enemyX_moving[i]
    if enemyX[i] >= rightEnemyBoundary or enemyX[i] <= leftBoundary:
      enemyX_moving[i] *= -1
      enemyY[i] += enemyY_moving
    
    if isCollision(enemyX[i], enemyY[i], bulletX, bulletY)and bulletState is"fire":
      bulletState = "ready"
      bulletY = playerY
      enemyX[i], enemyY[i] = random.randint(leftBoundary, rightEnemyBoundary-1), random.randint(40, 100)
      score += 1
      increaseSpeed(score)
      # update the score (update on surface)
      text = font.render(f"Score: {score}", True, (255, 255, 255))

    enemy(enemyX[i], enemyY[i])

  if bulletState is "fire" and bulletY > upperBoundary:
    Bullet(bulletX, bulletY)
    bulletY += bulletY_moving
  else:
    bulletState = "ready"
    bulletY = playerY

  player(playerX, playerY)

  # display the score (display surface)
  screen.blit(text, (textX, textY))

  pygame.display.update()