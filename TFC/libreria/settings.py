from typing import Tuple
import pygame


#COLOURS AND WINDOW SETTINGS

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 600, 700       # SCREEN

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREY = [128, 128, 128]
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]
TEXTCOLOR = [0, 0, 0]
GRAY = GREY

FPS = 240                # Limitar velocidad del programa y dibujo

ROWS = COLS = 50         #Resolucion

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE              # Background

DRAW_GRID_LINES = False            # Mejor sin que se vean


def get_font(size):
    return pygame.font.SysFont("comicsans", size)    # Fuente de texto



