import pandas as pd
from PIL import Image
from IPython.display import display


def table_to_image(size, table_name, save_name):
    table = pd.read_csv(table_name, header=None).to_numpy()
    img = Image.new('RGB', (size, size), "black")
    pixels = img.load()

    max_value = 2 * size - 1
    normalizer = 1 / max_value
    for i in range(size):
        for j in range(size):
            normalized_table_value = table[i][j] * normalizer
            pixel_value = int(255 * (1 - normalized_table_value))
            pixels[i, j] = (pixel_value, 0, pixel_value)
    img.save(save_name, format="png")


# table_to_image(100, "L.csv", "visual.png")
table_to_image(250, "Nim.csv", "Nim.png")