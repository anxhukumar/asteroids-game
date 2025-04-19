import pygame
from constants import *
from player import Player

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
    
    # limit FPS to 60
    delta = clock.tick(60)
    dt = delta/1000

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    player.draw(screen)
    pygame.display.flip()

if __name__ == "__main__":
  main()