
import cv2
from mss import mss, tools
from PIL import Image
import numpy as np

class ScreenReader:
    def __init__(self, top, left, width, height):
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
class ScreenReader:
    def __init__(self, top, left, width, height):
        with mss() as sct:
            # The screen part to capture
            monitor = {"top": top, "left": left, "width": width, "height": height}
            output_gray = "sct-{top}x{left}_{width}x{height}_gray.png".format(**monitor)

            # Grab the data
            sct_img = sct.grab(monitor)

            # Convert to PIL Image
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

            # Convert to grayscale
            self.gray_img = img.convert('L')
            print("Image is gray scaled")

            # Save grayscale image
            self.gray_img.save(output_gray)
            print("Grayscale:", output_gray)
    '''

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
                    row_state.append(0)  # Cell is empty
            board_state.append(row_state)
        return board_state
