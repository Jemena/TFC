from typing import Dict
from pygame import Color
from libreria import *
import json



WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))   # Window --> editar en settings
pygame.display.set_caption("Paint Chapuza")

def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])         # Añadir fila
        for _ in range(cols):
            grid[i].append(color)  # Añadir colores en fila

    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):                              # i, j posiciones de los pixel
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i *
                                          PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):        # +1 es para q hayan lineas en los finales
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid, buttons):   # Color y update canvas
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


def get_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE                # Cuidado el orden de filas y columnas
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


run = True
clock = pygame.time.Clock()

grid = init_grid(ROWS, COLS, BG_COLOR)       # Pixels
drawing_color = BLACK

#print(grid)

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, BLUE),
    Button(250, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(310, button_y, 50, 50, WHITE, "Clear", BLACK),
    Button(370, button_y, 50, 50, GREY, "Save", BLACK),
    Button(430, button_y, 50, 50, GREY, "Load", BLACK)
]

datos = list()

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:  # 0 click izq, 1 rueda, 2 click der
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_pos(pos)
                grid[row][col] = drawing_color
                #pixels = {'pos': [], 'color': [] }
                #pixels['pos'].append(get_pos(pos))
                #pixels['color'].append(drawing_color)
                #datos.append(pixels)
                #print(grid)
                
            except IndexError:
                
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    drawing_color = button.color
                    
                    if button.text == "Clear":
                        datos.clear()
                        grid = init_grid(ROWS, COLS, BG_COLOR)        #desde settings
                        drawing_color = BLACK
                        print("Todo limpio")
                    
                    if button.text == "Save":
                        datos.clear()
                        datos.extend(grid)
                        drawing_color = BLACK
                        with open('paint.json', 'w') as saved_data:
                            json.dump(datos, saved_data)
                        #print(datos)
                    
                    if button.text == "Load":
                        drawing_color = BLACK
                        with open('paint.json', 'r') as saved_data:
                           datos = json.load(saved_data)
                        for dato in datos:
                            grid = []
                            grid= datos
                        #print(datos)
                        
                        
    draw(WINDOW, grid, buttons)

pygame.quit()
print("Cerrando la chapuza")
