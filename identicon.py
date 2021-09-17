#!/usr/bin/env python

from PIL import Image, ImageDraw
from hashlib import md5
import sys
from datetime import datetime

GRID_SIZE = 5
SQUARE_SIZE = GRID_SIZE * 10
BORDER_SIZE = SQUARE_SIZE // 2

class Identicon(object):
    def __init__(self, istring, background='#e4e4e4'):
        """
        `istring` is the string used to generate the identicon.
        `background` is the background of the identicon.
        """

        self.identicon_data:dict = self.__set_identicon_data(istring)
        
        w = h = BORDER_SIZE * 2 + SQUARE_SIZE * GRID_SIZE
        self.image = Image.new('RGB', (w, h), background)
        self.draw = ImageDraw.Draw(self.image)


    def __set_hash(self, istring: str):
        return list(bytearray(md5(str(istring).encode('utf-8')).digest()))

    def __set_grid(self, hash_list):
        grid = []

        for i in range(0, len(hash_list)-3, 3):
            tmp = [hash_list[i], hash_list[i+1], hash_list[i+2], hash_list[i+1], hash_list[i]]
            grid.append(tmp)

        return grid
    
    def __set_identicon_data(self, istring):
        identicon_data = dict()

        identicon_data['istring'] = istring
        identicon_data['hash'] = self.__set_hash(identicon_data['istring'])
        identicon_data['rgb'] = tuple(identicon_data['hash'][:3])
        identicon_data['grid'] = self.__set_grid(identicon_data['hash'])

        return identicon_data

    def calculate(self):
        square_x = square_y = 0

        color = self.identicon_data['rgb']
        grid = self.identicon_data['grid']

        for i in range(GRID_SIZE):
            for j in range(len(grid[i])):
                if grid[i][j] % 2 == 0:
                    x = BORDER_SIZE + square_x * SQUARE_SIZE
                    y = BORDER_SIZE + square_y * SQUARE_SIZE
                    
                    self.draw.rectangle(
                        (x, y, x + SQUARE_SIZE, y + SQUARE_SIZE),
                        fill=color,
                        outline=color
                    )
                
                square_x += 1
                
                if square_x == GRID_SIZE:
                    square_x = 0
                    square_y += 1

    def get_image(self):
        self.calculate()
        self.image.show()

    def save_image(self, path_to_save:str='identicon.png'):
        self.calculate()
        
        with open(path_to_save, 'wb') as out:
            self.image.save(out, 'PNG')
        

def main():
    istring = 'identicon.png'

    idcon = Identicon(istring)
    # idcon.get_image()
    # idcon.save_image()

if __name__ == "__main__":
    main()