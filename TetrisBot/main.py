import cv2
from ScreenReader import ScreenReader
from keyboardInteraction import KeyboardInput
import keyboard
import time

next_shape_coords = [632, 162]
current_shape_coords = [343, 56]

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    keyboard = KeyboardInput()

    #while True:
    #    keyboard.press_space()

    # Get the current state of the board
    while True:
        time.sleep(0.5)
        screenShot = ScreenReader(180, 600, 750, 800)
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


