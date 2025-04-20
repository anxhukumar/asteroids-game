import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  dt = 0

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)
  player = Player(x, y)
  asteroidfield = AsteroidField()

  while(True):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return 
    
    # limit FPS to 60
    delta = clock.tick(60)
    dt = delta/1000 

    # updating the sprites
    updatable.update(dt)

    for items in asteroids:
      if items.collision(player):
        print("Game over!")
        sys.exit()

    screen.fill("black")
    
    # adding player to screen
    for item in drawable:
      item.draw(screen)
    
    # update the screen
    pygame.display.flip()
    
if __name__ == "__main__":
  main()