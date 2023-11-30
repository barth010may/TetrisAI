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
held_shape_pixel = [95, 168]

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

TETROMINO_HELD = {
    (62, 167, 192): Tetromino.OTetromino(),
    (147, 194, 64): Tetromino.ITetromino(),
    (167, 74, 177): Tetromino.TTetromino(),
    (65, 195, 146): Tetromino.STetromino(),
    (72, 65, 195): Tetromino.ZTetromino(),
    (64, 114, 195): Tetromino.LTetromino(),
    (177 ,74, 91): Tetromino.JTetromino()
}



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    keyboard = KeyboardInput()
    first_screenshot = ScreenReader(180, 600, 750, 800)
    current_tetromino = TETROMINO_CURRENT[first_screenshot.get_pixel(current_shape_pixel)]
    next_tetromino = None
    time.sleep(0.2)
    flag = True
    '''
    while True:
        if (input() == 'q'):
            ss = ScreenReader(180, 600, 750, 800)
            ss.get_pixel(held_shape_pixel)
    '''
    
    while True:
        
        screenShot = ScreenReader(180, 600, 750, 800)
        next_tetromino = TETROMINO_NEXT[screenShot.get_pixel(next_shape_pixel)]
        
        # holds the first piece of the round, to have something to compare with
        if (flag == True):
            pyautogui.press('c')
            pyautogui.press(' ')
            flag = False
            current_tetromino = next_tetromino
            continue
        
        held_tetromino = TETROMINO_HELD[screenShot.get_pixel(held_shape_pixel)]
        
        # get the current state of the board into a 2D array
        current_board_state = screenShot.get_board_state(grid_size, cell_size, board_dimensions)
        field = Field(current_board_state)
        print(field)
        
        opt_current = Optimizer.get_optimal_drop(field, current_tetromino)
        # TODO: Implement Held piece, to optimize algorithm. Just compare the drop of both pieces and determine which is better
        # For the start of the round, just auto place the first piece into the held spot, since it doesn't make a big difference
        opt_held = Optimizer.get_optimal_drop(field, held_tetromino)
        
        held_tet_better = opt_held['cost'] < opt_current['cost']
        if (held_tet_better):
            opt = opt_held
        else:
            opt = opt_current
        
        rotation = opt['tetromino_rotation']
        column = opt['tetromino_column']
        
        keys = Optimizer.get_keystrokes(rotation, column, {
            'rotate_right': 'x',
            'rotate_left': 'z',
            'move_left': 'left',
            'move_right': 'right',
            'drop': ' '
        })
        if (held_tet_better):
            keys.insert(0, 'c')
        pyautogui.typewrite(keys)
        current_tetromino = next_tetromino
        time.sleep(0.5)
    
        

