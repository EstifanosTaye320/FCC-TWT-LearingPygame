import pygame

# start the package
pygame.init()

# create your screen
screen = pygame.display.set_mode((800, 600))

# how to create a game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False