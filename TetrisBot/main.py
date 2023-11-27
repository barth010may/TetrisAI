import cv2
from ScreenReader import ScreenReader
from keyboardInteraction import KeyboardInput
import keyboard
import time
from Shape import Tetromino
import pyautogui
import numpy as np
from optimizer import Optimizer
from field import Field

next_shape_pixel = [642, 173]
current_shape_pixel = [335, 50]

# Define the Tetris board area coordinates and size
board_top = 92
board_left = 208
board_width = 515 - board_left
board_height = 738 - board_top
cell_width = 343 - 308
cell_height = 34
# Define the grid size and cell size
grid_size = (10, 20)  # Example for a standard Tetris grid
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
TETROMINO_CURRENT = {
    (60, 205, 241): Tetromino.OTetromino(),
    (172, 238,  57): Tetromino.ITetromino(),
    (207 , 79, 221): Tetromino.TTetromino(),
    (59, 240, 171): Tetromino.STetromino(),
    ( 72,  62, 245): Tetromino.ZTetromino(),
    (61, 129, 243): Tetromino.LTetromino(),
    (221 , 79, 104): Tetromino.JTetromino()

}

TETROMINO_NEXT = {
    (56,149, 171): Tetromino.OTetromino(),
    (115, 152,  50): Tetromino.ITetromino(),
    (155, 63, 165): Tetromino.TTetromino(),
    (51, 180, 132): Tetromino.STetromino(),
    ( 59,  52, 181): Tetromino.ZTetromino(),
    (51, 100, 180): Tetromino.LTetromino(),
    (165,  63,  80): Tetromino.JTetromino()
}



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    keyboard = KeyboardInput()
    current_tetromino = TETROMINO_CURRENT[ScreenReader.get_pixel(current_shape_pixel)]
    next_tetromino = None
    time.sleep(2)
        
    # Get the current state of the board
    while True:
        next_tetromino = TETROMINO_NEXT[ScreenReader.get_pixel(next_shape_pixel)]
        current_board_state = ScreenReader(180, 600, 750, 800).get_board_state(grid_size, cell_size, board_dimensions)
        #ScreenReader.print_board(current_board_state)
        
        field = Field(current_board_state)
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
        ScreenReader.print_board(current_board_state)
        current_tetromino = next_tetromino
        time.sleep(0.001)
        

