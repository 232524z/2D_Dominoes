import numpy as np
import pandas as pd


class L:
    table = None
    dimensions = None

    def __init__(self, table_size):
        self.table = np.array([[0] * table_size] * table_size)
        self.dimensions = table_size

    def __repr__(self):
        return str(self.table)

    # Finds the minimum excluded value from an array
    @staticmethod
    def mex(options):
        for i in range(len(options)):
            try:
                options.index(i)
            except ValueError:
                return i
        return len(options) + 1

    # Sums two nimbers using an XOR on each digit of binary
    @staticmethod
    def nim_sum(nim1, nim2):
        nim1, nim2 = bin(nim1)[2:], bin(nim2)[2:]
        sum = 0
        length = max(len(nim1), len(nim2))
        for i in range(1, length + 1):
            try:
                digit1 = int(nim1[-i])
            except:
                digit1 = 0

            try:
                digit2 = int(nim2[-i])
            except:
                digit2 = 0

            if digit1 != digit2:
                sum += 2 ** (i - 1)
        return sum

    def get_table(self):
        return self.table

    def set_value(self, row, col, value):
        row, col = row - 1, col - 1
        self.table[row][col] = value
        self.table[col][row] = value

    def get_value(self, row, col):
        if row == 0 or col == 0:
            return 0
        return self.table[row - 1][col - 1]

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
            dominoes_to_the_left = index-height+1
            dominoes_to_the_right = width-dominoes_to_the_left-1
            left = self.nim_sum(height-1, dominoes_to_the_right)
            right = self.get_value(height, dominoes_to_the_left)
            out = self.nim_sum(right, dominoes_to_the_right)
            options = [left, right, out]

        return options

    def to_dataframe(self):
        df = pd.DataFrame(self.table)
        return df