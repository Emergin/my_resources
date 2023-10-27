import pygame
import sys

# Constants
TILE_SIZE = 40
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Game objects
WALL = '#'
PLAYER = '@'
BOX = '$'
TARGET = '.'

# Sample map
MAP = [
    "#########",
    "#@ $    #",
    "#   ### #",
    "#     $ #",
    "#    ### ",
    "#########"
]

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sokoban')

def draw_game():
    screen.fill(WHITE)
    for y, row in enumerate(MAP):
        for x, char in enumerate(row):
            if char == WALL:
                pygame.draw.rect(screen, BLUE, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif char == PLAYER:
                pygame.draw.circle(screen, RED, (x*TILE_SIZE + TILE_SIZE//2, y*TILE_SIZE + TILE_SIZE//2), TILE_SIZE//2 - 5)
            elif char == BOX:
                pygame.draw.rect(screen, GREEN, (x*TILE_SIZE + 5, y*TILE_SIZE + 5, TILE_SIZE - 10, TILE_SIZE - 10))
            elif char == TARGET:
                pygame.draw.circle(screen, BLACK, (x*TILE_SIZE + TILE_SIZE//2, y*TILE_SIZE + TILE_SIZE//2), 5)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_game()
        pygame.display.flip()

if __name__ == "__main__":
    main()

