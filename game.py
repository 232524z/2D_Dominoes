import numpy as np
import pandas as pd
from PIL import Image


class Game:
    def __init__(self, table_size):
        self.table = np.array([[0] * table_size] * table_size)
        self.dimensions = table_size

    def __repr__(self):
        return str(self.table)

    # Finds the minimum excluded value from an array
    @staticmethod
    def mex(options):
        # Initially, every value is excluded
        excluded_array = [True for i in range(len(options)+1)]

        # For every option, marks that option as not being excluded
        for option in options:
            excluded_array[option] = False

        # Finds the first excluded value in the array
        for i in range(len(excluded_array)):
            if excluded_array[i]:
                return i

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

    def import_csv(self, csv_name):
        self.table = pd.read_csv(csv_name, header=None).to_numpy()

    def save_image(self, save_name):
        img = Image.new('RGB', (self.dimensions, self.dimensions), "black")
        pixels = img.load()

        # The largest L has 2*self.dimensions - 1 total dominoes, so it is not possible for a nim value to be greater
        # than that value
        max_value = 2 * self.dimensions - 1

        # Multiplying a nim value by the normalizer will return something in (0,1]
        normalizer = 1 / max_value

        for i in range(self.dimensions):
            for j in range(self.dimensions):
                # Normalizes all values
                normalized_table_value = self.table[i][j] * normalizer

                # Bright colors correspond to low values
                pixel_value = int(255 * (1 - normalized_table_value))
                pixels[i, j] = (pixel_value, 0, pixel_value)
        img.save(save_name, format="png")