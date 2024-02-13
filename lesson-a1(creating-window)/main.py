import pygame
# control the system inbuilt
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
icon = pygame.image.load('./assets/images/home.png')
pygame.display.set_icon(icon)

# used to control framerate
clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      # ending pygame.init()
      pygame.quit()
      
      # ending the current program
      exit()
    
  pygame.display.update()
  
  # setting the framerate to about 60 per sec (max framerate)
  clock.tick(60)