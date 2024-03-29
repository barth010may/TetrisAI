#!/usr/bin/python

from Shape import Tetromino

from collections import defaultdict
from functools import cmp_to_key
from field import Field

class Optimizer():
    
    @staticmethod
    def get_optimal_drop(field, tetromino):
        rotations = [
            tetromino,
            tetromino.copy().rotate_right(),
            tetromino.copy().flip(),
            tetromino.copy().rotate_left(),
        ]
        drops = []
        for rotation, tetromino_ in enumerate(rotations):
            for column in range(Field.WIDTH):
                try:
                    f = field.copy()
                    row = f.drop(tetromino_, column)
                    drops.append({
                        'field': f,
                        'field_gaps': f.count_gaps(),
                        'field_height': f.height(),
                        'tetromino_rotation': rotation,
                        'tetromino_column': column,
                        'tetromino_row': row
                    })
                except AssertionError:
                    continue
        
        # TODO: Long boy, always places the tet one column to the right of the optimal drop, could be a index problem
        # where the column count from 1 and the field counts from 0, seems to work when column tet is subtracted by 1, but it fucks up the rest of the field
        
        # Calculate the cost of every drop, and return the drop which cost is the lowest 
        
        for drop in drops:
            #print(drop['field'])
            #print(f'field height: {drop["field_height"]}')
            #print(f'amount of gaps: {drop["field_gaps"]}')
            #print(f'lowest row: {drop["tetromino_row"]}') 
            drop['cost'] = drop['field_gaps'] + 2 * drop['field_height']
            print(f'cost: {drop["cost"]}')
        
        # sort the drops based on the lowest cost first.
        drops.sort(key=lambda drop: drop['cost'])
        
        print(drops[0]['field'])
        print(f'lowest cost drop: {drops[0]["cost"]}')
        
        '''
        #First, we pick out all the drops that will produce the least
        #amount of gaps.
        lowest_gaps = min([drop['field_gaps'] for drop in drops])
        drops = list(filter(
            lambda drop: drop['field_gaps'] == lowest_gaps, drops))
        # Next we sort for the ones with the lowest field height.
        lowest_height = min([drop['field_height'] for drop in drops])
        drops = list(filter(
            lambda drop: drop['field_height'] == lowest_height, drops))
        
        # Finally, we sort for the ones that drop the tetromino in the lowest
        # row. Since rows increase from top to bottom, we use max() instead.
        lowest_row = max([drop['tetromino_row'] for drop in drops])
        drops = list(filter(
            lambda drop: drop['tetromino_row'] == lowest_row, drops))
        '''
        
        assert len(drops) > 0
        return drops[0]

    @staticmethod
    def get_keystrokes(rotation, column, keymap):
        keys = []
        # First we orient the tetronimo
        if rotation == 1:
            keys.append(keymap['rotate_right'])
        elif rotation == 2:
            keys.append(keymap['rotate_right'])
            keys.append(keymap['rotate_right'])
        elif rotation == 3:
            keys.append(keymap['rotate_right'])
            keys.append(keymap['rotate_right'])
            keys.append(keymap['rotate_right'])
        # Then we move it all the way to the the left that we are guaranteed
        # that it is at column 0. The main reason for doing this is that when
        # the tetromino is rotated, the bottom-leftmost piece in the tetromino
        # may not be in the 3rd column due to the way Tetris rotates the piece
        # about a specific point. There are too many edge cases so instead of
        # implementing tetromino rotation on the board, it's easier to just
        # flush all the pieces to the left after orienting them.
        for i in range(6):
            keys.append(keymap['move_left'])
        # Now we can move it back to the correct column. Since pyautogui's
        # typewrite is instantaneous, we don't have to worry about the delay
        # from moving it all the way to the left.
        for i in range(column):
            keys.append(keymap['move_right'])
        keys.append(keymap['drop'])
        return keys

'''
if __name__ == '__main__':
    f = Field()
    f.drop(Tetromino.TTetromino(), 3)
    opt = Optimizer.get_optimal_drop(
        f['tetromino_rotation'], f['tetromino_column'], Tetromino.ITetromino())
    print(opt['field'])
'''