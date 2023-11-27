
import cv2
from mss import mss, tools
from PIL import Image, ImageOps
import numpy as np
import pyautogui

class ScreenReader:
    def __init__(self, top, left, width, height):
        
        # Capture a specific region of the screen
        # The region is defined by (left, top, width, height)
        
        region = (left, top, width, height)  # Example values
        screenshot = pyautogui.screenshot(region=region)
        
        # Convert the screenshot to grayscale
        #gray_screenshot = ImageOps.grayscale(screenshot)

        # Convert to NumPy array in BGR format
        img = np.array(screenshot)
        
        # Convert BGR to Grayscale
        self.gray_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

        # Save grayscale image
        cv2.imwrite('grayscale_screenshot.png', self.gray_img)
        print("Grayscale:", 'grayscale_screenshot.png')

        # Save the grayscale screenshot
        #screenshot.save('grayscale_screenshot.png')
        
        '''
        with mss() as sct:
            # The screen part to capture
            monitor = {"top": top, "left": left, "width": width, "height": height}
            output_gray = "sct-{top}x{left}_{width}x{height}_gray.png".format(**monitor)

            # Grab the data
            sct_img = sct.grab(monitor)

            # Convert to NumPy array in BGR format
            img = np.array(sct_img)

            # Convert BGR to Grayscale
            self.gray_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

            print("Image is gray scaled")

            # Save grayscale image
            cv2.imwrite(output_gray, self.gray_img)
            print("Grayscale:", output_gray)
            '''

    def get_pixel(coords):
    
        # Capture a specific region of the screen
        # The region is defined by (left, top, width, height)
        
        region = (600, 180, 750, 800)  # Example values
        screenshot = pyautogui.screenshot(region=region)

        # Convert to NumPy array in BGR format
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        # Convert BGR to Grayscale
        #gray_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        cv2.imwrite('grayscale_screenshot.png', img)
        print("Grayscale:", 'grayscale_screenshot.png')
        
        pixel_value = img[coords[1], coords[0]]
        print(f"Pixel Value: {pixel_value}")
        return tuple(pixel_value)

    # Load an image in gray scale
    def grayScale_pixels(self, coords):

        #tempFile = cv2.imread("sct-180x600_750x800_gray1.png", cv2.IMREAD_GRAYSCALE)
        #pixel_value = tempFile[coords[1], coords[0]]

        pixel_value = self.gray_img[coords[1], coords[0]]
        return pixel_value


    def is_cell_filled(self, cell):
        if self.grayScale_pixels(cell) != 0:
            return True
        else:
            return False

    @staticmethod
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
                    row_state.append(1)  # Cell is filled
                else:
                    row_state.append(' ')  # Cell is empty
            board_state.append(row_state)
        return board_state
