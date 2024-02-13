import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
font = pygame.font.Font("./assets/font/pixeltype.ttf", 50)

# convert method used to make the image something that pygame can work with better
sky_surface = pygame.image.load("./assets/graphics/sky.png").convert()
ground_surface = pygame.image.load("./assets/graphics/ground.png").convert()
font_surface = font.render("My game", False, (0, 0, 0))

# convert_alpha method used to deal with the black and white behind the image
snail_surface = pygame.image.load("./assets/graphics/snail/snail1.png").convert_alpha()
snailX, snailY = 600, 260
snailX_moving = -4

def snailEnemy(x, y):
  screen.blit(snail_surface, (x, y))

clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      pygame.quit()
      exit()

  snailX += snailX_moving
  if snailX < -100:
    snailX = 800

  screen.blit(sky_surface, (0, 0))
  screen.blit(ground_surface, (0, 300))
  screen.blit(font_surface, (350, 20))
  screen.blit(snail_surface, (snailX, snailY))

  pygame.display.update()
  clock.tick(60)