import pygame

# Can be freely configure

NUMBER_OF_ROWS = 9
NUMBER_OF_COLUMNS = 9
NUMBER_OF_MINES = 10

# Defines index 0: columns, index 1: rows, index 2: mines
DIFFICULTIES = {
    1: [9,9,10],
    2: [16,16,40],
    3: [30,16,99],
    4: [30,30,225]
}

# UI configuration

SIZE_OF_SQUARE = 40
BOARD_WIDTH = SIZE_OF_SQUARE * NUMBER_OF_COLUMNS
BOARD_HEIGHT = SIZE_OF_SQUARE * NUMBER_OF_ROWS
UI_WIDTH = 200
WINDOW_WIDTH = BOARD_WIDTH + UI_WIDTH

def calculate_UI_config():
    global BOARD_WIDTH, BOARD_HEIGHT, WINDOW_WIDTH
    
    BOARD_WIDTH = SIZE_OF_SQUARE * NUMBER_OF_COLUMNS
    BOARD_HEIGHT = SIZE_OF_SQUARE * NUMBER_OF_ROWS
    WINDOW_WIDTH = BOARD_WIDTH + UI_WIDTH

def revert_default_UI_config():
    global BOARD_WIDTH, BOARD_HEIGHT, WINDOW_WIDTH
    
    BOARD_WIDTH = SIZE_OF_SQUARE * 9
    BOARD_HEIGHT = SIZE_OF_SQUARE * 9
    WINDOW_WIDTH = BOARD_WIDTH + UI_WIDTH

# Main colors
COLOR_BACKGROUND = (100,100,100)
COLOR_OPEN_SQUARE = (220,220,220)
COLOR_CLOSED_SQUARE = (160,160,160)
COLOR_FRAME = (160,160,160)
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_RED = (255,0,0)
COLOR_LIGHT_GRAY = (90,90,90)
COLOR_DARK_GRAY = (20,20,20)
COLOR_SELECTED = (60,60,60)

# Colors of numbers
COLOR_1 = (0, 0, 255)
COLOR_2 = (0, 128, 0)
COLOR_3 = (255, 0, 0)
COLOR_4 = (0, 0, 128)
COLOR_5 = (128, 0, 0)
COLOR_6 = (0, 128, 128)
COLOR_7 = (0, 0, 0)
COLOR_8 = (128, 128, 128)

# Other
FONT_CONFIG = None # needs to be set after pygame.init
GAME_NAME = "Minesweeper"
FPS = 20

def set_pygame_config():
    global FONT_CONFIG
    
    if not pygame.font.get_init():
        pygame.font.init()
    
    FONT_CONFIG = pygame.font.SysFont("arial", 20, True)
    pygame.display.set_caption(GAME_NAME)
    screen = pygame.display.set_mode((WINDOW_WIDTH, BOARD_HEIGHT))
    
    return screen