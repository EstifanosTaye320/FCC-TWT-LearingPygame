import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
font = pygame.font.Font("./assets/font/pixeltype.ttf", 50)

sky_surface = pygame.image.load("./assets/graphics/sky.png").convert()
ground_surface = pygame.image.load("./assets/graphics/ground.png").convert()
font_surface = font.render("My game", False, (0, 0, 0))

snail_surface = pygame.image.load("./assets/graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomleft = (600, 300))
snailX_moving = -4

# how to use a rectangle for positioning
player_surface = pygame.image.load("./assets/graphics/player/player_walk_1.png")
player_rectangle = player_surface.get_rect(midbottom = (80, 300))

clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      pygame.quit()
      exit()

  # how to set surface movement using a rectangle
  snail_rectangle.left += snailX_moving
  if snail_rectangle.right < 0:
    snail_rectangle.left = 800

  screen.blit(sky_surface, (0, 0))
  screen.blit(ground_surface, (0, 300))
  screen.blit(font_surface, (350, 20))
  screen.blit(snail_surface, snail_rectangle)
  
  # blit() method with the rectangle as a coordinate
  screen.blit(player_surface, player_rectangle)

  pygame.display.update()
  clock.tick(60)