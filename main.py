import pygame
from constants import *
from player import Player

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  dt = 0

  Player.containers = (updatable, drawable)
  player = Player(x, y)

  while(True):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return 
    
    # limit FPS to 60
    delta = clock.tick(60)
    dt = delta/1000 

    # updating the sprites
    updatable.update(dt)

    screen.fill("black")
    
    # adding player to screen
    for item in drawable:
      item.draw(screen)
    
    # update the screen
    pygame.display.flip()
    
if __name__ == "__main__":
  main()