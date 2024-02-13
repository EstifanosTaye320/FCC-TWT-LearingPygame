import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
font = pygame.font.Font("./assets/font/pixeltype.ttf", 50)

# regular surfaces for color, image and text
# color_surface = pygame.Surface(100, 200)
# color_surface.fill("green")
sky_surface = pygame.image.load("./assets/graphics/sky.png")
ground_surface = pygame.image.load("./assets/graphics/ground.png")
font_surface = font.render("My game", False, (0, 0, 0))

clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      pygame.quit()
      exit()
  
  # place regular surface on to dispaly surface
  # screen.blit(color_surface, (200, 100))
  screen.blit(sky_surface, (0, 0))
  screen.blit(ground_surface, (0, 300))
  screen.blit(font_surface, (350, 20))
  
  pygame.display.update()
  clock.tick(60)