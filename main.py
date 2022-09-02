import itertools
import pygame

from chessPieces import *

pygame.init()

SCREEN_WIDTH = SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (150, 75, 0)
RED = (165, 42, 42)


def main():

    run = True

    tile_size = 75
    width, height = 8 * tile_size, 8 * tile_size
    background = pygame.Surface((width, height))
    colors = itertools.cycle((WHITE, BROWN))
    clock = pygame.time.Clock()

    while run:

        # BLACK BACK PART
        screen.blit(black_ROOK, (8, 10))
        screen.blit(black_KNIGHT, (80, 10))
        screen.blit(black_BISHOP, (160, 10))
        screen.blit(black_KING, (230, 10))
        screen.blit(black_QUEEN, (310, 10))
        screen.blit(black_BISHOP, (385, 10))
        screen.blit(black_KNIGHT, (455, 10))
        screen.blit(black_ROOK, (535, 10))

        # BLACK FRONT PART
        screen.blit(black_PAWN, (8, 80))
        screen.blit(black_PAWN, (80, 80))
        screen.blit(black_PAWN, (160, 80))
        screen.blit(black_PAWN, (230, 80))
        screen.blit(black_PAWN, (310, 80))
        screen.blit(black_PAWN, (385, 80))
        screen.blit(black_PAWN, (455, 80))
        screen.blit(black_PAWN, (535, 80))

        # WHITE BACK PART
        screen.blit(white_ROOK, (8, 535))
        screen.blit(white_KNIGHT, (80, 535))
        screen.blit(white_BISHOP, (160, 535))
        screen.blit(white_KING, (230, 535))
        screen.blit(white_QUEEN, (310, 535))
        screen.blit(white_BISHOP, (385, 535))
        screen.blit(white_KNIGHT, (455, 535))
        screen.blit(white_ROOK, (535, 535))

        # WHITE FRONT PART
        screen.blit(white_PAWN, (8, 460))
        screen.blit(white_PAWN, (80, 460))
        screen.blit(white_PAWN, (160, 460))
        screen.blit(white_PAWN, (230, 460))
        screen.blit(white_PAWN, (310, 460))
        screen.blit(white_PAWN, (385, 460))
        screen.blit(white_PAWN, (455, 460))
        screen.blit(white_PAWN, (535, 460))

        pygame.display.update()

        # CHESS BOARD
        for y in range(0, height, tile_size):
            for x in range(0, width, tile_size):
                rect = (x, y, tile_size, tile_size)
                pygame.draw.rect(background, next(colors), rect)
            next(colors)

        # QUIT GAME
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Fin Du Jeu")
                pygame.quit()

        screen.blit(background, (0, 0))
        clock.tick(30)


main()
