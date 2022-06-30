import json
from PIL import Image
from progressbar import progressbar as bar
from IPython.display import display
from math import log, sqrt

print("Imported.")
f = open('data.json')

print("Open complete. Beginning loading.")
data = json.load(f)
print("Loaded.")



def purple_image(name, function):
    size = 10000
    img = Image.new('RGB', (size, size), "black")
    pixels = img.load()

    max_value = function(2 * size - 1)
    normalizer = 1 / max_value
    for i in bar(range(size)):
        for j in range(size):
            normalized_table_value = function(data[i][j]) * normalizer
            pixel_value = int(255 * (1 - normalized_table_value))
            pixels[i, j] = (pixel_value, 0, pixel_value)
    img.save(name, format="png")

def color_image(name, function):
    size = 10000
    img = Image.new('HSV', (size, size), "black")
    pixels = img.load()

    max_value = function(2 * size - 1)
    normalizer = 1 / max_value
    for i in bar(range(size)):
        for j in range(size):
            normalized_table_value = function(data[i][j]) * normalizer
            pixel_value = int(360 * (1 - normalized_table_value))
            pixels[i, j] = (pixel_value, 255, 255)
    img = img.convert(mode="RGB")
    img.save(name, format="png")

def red_to_blue_image(name, function):
    size = 10000
    img = Image.new('RGB', (size, size), "black")
    pixels = img.load()

    max_value = function(2 * size - 1)
    normalizer = 1 / max_value
    for i in bar(range(size)):
        for j in range(size):
            normalized_table_value = function(data[i][j]) * normalizer
            red_pixel_value = int(255 * (1 - normalized_table_value))
            blue_pixel_value = int(255 * normalized_table_value)
            pixels[i, j] = (red_pixel_value, 0, blue_pixel_value)
    img.save(name, format="png")

# color_image("linear_color_image.png", lambda num: num)
color_image("log_color_image.png", lambda num: log(num))

# red_to_blue_image("sqrt_red_tp_blue_image.png", lambda num: sqrt(num))
