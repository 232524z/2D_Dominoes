import numpy as np
import pandas as pd
from game import Game

class L(Game):

    def __init__(self, table_size):
        super().__init__(table_size)

    def find_options(self, height, width, index):
        if index + 1 < height:
            up = self.get_value(height - (index + 1), width)
            down = self.nim_sum(index, width - 1)
            out = self.nim_sum(index, up)
            options = [up, down, out]

        if index + 1 == height:
            up = width - 1
            right = height - 1
            out = self.nim_sum(height - 1, width - 1)
            options = [up, right, out]

        if index + 1 > height:
            dominoes_to_the_left = index - height + 1
            dominoes_to_the_right = width - dominoes_to_the_left - 1
            left = self.nim_sum(height - 1, dominoes_to_the_right)
            right = self.get_value(height, dominoes_to_the_left)
            out = self.nim_sum(right, dominoes_to_the_right)
            options = [left, right, out]

        return options
