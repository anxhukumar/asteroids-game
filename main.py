import pygame
from constants import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  dt = 0
  clock = pygame.time.Clock()

  while(True):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return 
    
    screen.fill("black")
    pygame.display.flip()

    # limit FPS to 60
    delta = clock.tick(60)
    dt = delta/1000

if __name__ == "__main__":
  main()