import numpy as np
import pandas as pd


class Game:
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
        return nim1 ^ nim2


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

    def to_dataframe(self):
        df = pd.DataFrame(self.table)
        return df

    def save_csv(self, name):
        self.to_dataframe().to_csv(name, index=False, header=False)
