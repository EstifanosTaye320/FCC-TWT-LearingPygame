import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# icon and title
pygame.display.set_caption("Space Invaidors")
icon = pygame.image.load("./lesson-2(title-logo-bgc)/images/ufo.png")
pygame.display.set_icon(icon)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # adding a color to the screen
  screen.fill((0, 0, 0))

  # update screen on change
  pygame.display.update()