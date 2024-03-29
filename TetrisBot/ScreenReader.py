
import cv2
from PIL import Image, ImageOps
import numpy as np
import pyautogui

class ScreenReader:
    
    def __init__(self, top, left, width, height):
        
        # Capture a specific region of the screen
        # The region is defined by (left, top, width, height)
        
        region = (left, top, width, height)  # Example values
        screenshot = pyautogui.screenshot(region=region)

        # Convert to NumPy array in BGR format
        img = np.array(screenshot)
        
        # Convert BGR to Grayscale
        self.img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        # Save grayscale image
        cv2.imwrite('screenshot.png', self.img)
        print("Image Saved:", 'screenshot.png')
    
    def get_pixel(self, coords):
        pixel_value = self.img[coords[1], coords[0]]
        #print(f"Pixel Value: {pixel_value}")
        return tuple(pixel_value)

    def is_cell_filled(self, cell):
        if self.get_pixel(cell) != (0, 0, 0):
            return True
        else:
            return False

    def get_board_state(self, grid_size, cell_size, board_dimensions):
        board_state = []
        for row in range(grid_size[1]):  # grid_size[1] is the number of rows
            row_state = []
            for col in range(grid_size[0]):  # grid_size[0] is the number of columns

                x = col * cell_size[0] + board_dimensions[1]
                y = row * cell_size[1] + board_dimensions[0]

                cell = (x, y)
                #print(cell)

                # Determine if the cell is filled based on the image
                if self.is_cell_filled(cell):  # This threshold might need adjustment
                    row_state.append('q')  # Cell is filled
                else:
                    row_state.append(' ')  # Cell is empty
            board_state.append(row_state)
        return board_state
    
    @staticmethod
    def print_board(board):
        border_length = len(board[0]) * 2  # Each cell becomes two characters wide
        horizontal_border = '+' + '-' * border_length + '+'

        print(horizontal_border)  # Print top border
        for row in board:
            row_str = '|' + ''.join(["[]" if cell == 'q' else "  " for cell in row]) + '|'
            print(row_str)  # Print each row with vertical borders
        print(horizontal_border)  # Print bottom border
