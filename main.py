# this allow us to use code from
# the open-source pygame library
# throughout this file
# does it work? git?
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from constants import *


def main():
    # Initialize Pygame
    pygame.init()
    # Set up the drawing window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()

    



    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
