import pygame
import os

# BLACK PIECES
black_BISHOP = pygame.image.load(os.path.join("chess_Game/images", "bB.png"))
black_KING = pygame.image.load(os.path.join("chess_Game/images", "bK.png"))
black_KNIGHT = pygame.image.load(os.path.join("chess_Game/images", "bN.png"))
black_PAWN = pygame.image.load(os.path.join("chess_Game/images", "bp.png"))
black_QUEEN = pygame.image.load(os.path.join("chess_Game/images", "bQ.png"))
black_ROOK = pygame.image.load(os.path.join("chess_Game/images", "bR.png"))

# WHITE PIECES
white_BISHOP = pygame.image.load(os.path.join("chess_Game/images", "wB.png"))
white_KING = pygame.image.load(os.path.join("chess_Game/images", "wK.png"))
white_KNIGHT = pygame.image.load(os.path.join("chess_Game/images", "wN.png"))
white_PAWN = pygame.image.load(os.path.join("chess_Game/images", "wp.png"))
white_QUEEN = pygame.image.load(os.path.join("chess_Game/images", "wQ.png"))
white_ROOK = pygame.image.load(os.path.join("chess_Game/images", "wR.png"))
