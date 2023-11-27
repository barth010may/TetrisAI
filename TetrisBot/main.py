import cv2
from ScreenReader import ScreenReader
from keyboardInteraction import KeyboardInput
import keyboard
import time
from Shape import Tetromino
import pyautogui
import numpy as np

next_shape_pixel = [642, 173]
current_shape_pixel = [335, 50]

# Define the Tetris board area coordinates and size
board_top = 97 - 32 * 2
board_left = 212
board_width = 508 - board_left
board_height = 714 - board_top
cell_width = 244 - 212
cell_height = 244 - 212
# Define the grid size and cell size
grid_size = (10, 22)  # Example for a standard Tetris grid
cell_size = (cell_width, cell_height)
board_dimensions = (board_top, board_left)

''' HOME PC gray values, apparently they are different from screen to scree :(
def shape_gray_values(self):
        self.next_square = 146
        self.next_tower = 134
        self.next_pyramid = 108
        self.next_right_stair = 155
        self.next_left_stair = 96
        self.next_left_bed = 123
        self.next_right_bed = 84

        self.current_square = 182
        self.current_tower = 163, 
        self.current_pyramid = 117, 
        self.current_right_stair = 184
        self.current_left_stair = 99, 
        self.current_left_bed = 137
        self.current_right_bed = 81
'''

# True gray values for laptop screen
TETRIMINO_CURRENT = {
    (60, 205, 241): Tetromino.OTetromino,
    (172, 238,  57): Tetromino.ITetromino,
    (207 , 79, 221): Tetromino.TTetromino,
    (59, 240, 171): Tetromino.STetromino,
    ( 72,  62, 245): Tetromino.ZTetromino,
    (61, 129, 243): Tetromino.LTetromino,
    (221 , 79, 104): Tetromino.JTetromino
    
    #166: Tetromino.OTetromino,
    #198: Tetromino.ITetromino,
    #133: Tetromino.TTetromino,
    #178: Tetromino.STetromino,
    #86: Tetromino.ZTetromino,
    #122: Tetromino.LTetromino,
    #124: Tetromino.JTetromino
}

TETRIMINO_NEXT = {
    (56,149, 171): Tetromino.OTetromino,
    (115, 152,  50): Tetromino.ITetromino,
    (155, 63, 165): Tetromino.TTetromino,
    (51, 180, 132): Tetromino.STetromino,
    ( 59,  52, 181): Tetromino.ZTetromino,
    (51, 100, 180): Tetromino.LTetromino,
    (165,  63,  80): Tetromino.JTetromino
}



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    keyboard = KeyboardInput()
    screenShot = ScreenReader()
    current_tetromino = TETRIMINO_CURRENT[screenShot.get_pixel(current_shape_pixel)]
    next_tetromino = None
    time.sleep(2)
        
    # Get the current state of the board
    while True:
        next_tetromino = TETRIMINO_NEXT[screenShot.get_pixel(next_shape_pixel)]
        current_board_state = ScreenReader.get_board_state(grid_size, cell_size, board_dimensions)
        opt = Optimizer.get_optimal_drop(field, current_tetromino)
        rotation = opt['tetromino_rotation']
        column = opt['tetromino_column']
        #current_tetromino.rotate(rotation)
        #field.drop(current_tetromino, column)
        keys = Optimizer.get_keystrokes(rotation, column, {
            'rotate_right': 'x',
            'rotate_left': 'z',
            'move_left': 'left',
            'move_right': 'right',
            'drop': ' '
        })
        pyautogui.typewrite(keys)
        print(field)
        current_tetromino = next_tetromino
        time.sleep(0.2)
        
        
        
        '''
        time.sleep(0.1)
        screenShot = ScreenReader(180, 600, 750, 800)
        print("Screenshot taken!")
        
        current_board_state = screenShot.get_board_state(grid_size, cell_size, board_dimensions)
        #for row in current_board_state:
        #    print(''.join(["[]" if cell == 1 else " " for cell in row]))

        border_length = len(current_board_state[0]) * 2  # Each cell becomes two characters wide
        horizontal_border = '+' + '-' * border_length + '+'

        print(horizontal_border)  # Print top border
        for row in current_board_state:
            row_str = '|' + ''.join(["[]" if cell == 1 else "  " for cell in row]) + '|'
            print(row_str)  # Print each row with vertical borders
        print(horizontal_border)  # Print bottom border
        '''


