import pandas as pd
import json
import numpy as np
import pandas as pd
from L_Dominoes import L
from nimber import Nimber
from game import Game
import time

# table = pd.read_csv("L.csv", header=None).to_numpy()
# list = []
# for i in range (1,99, 2):
#    list.append(table[i][i])
# print(list)

#################################

# print("Imported.")
# f = open('data.json')
#
# print("Open complete. Beginning loading.")
# data = json.load(f)
# print("Loaded.")
#
# max_each_row = [max(row) for row in data]
# overall_max = max(max_each_row)
# print(overall_max)

####################################
# start = time.time()
# table_size = 100
# L_table = L(table_size)
# # Base cases for 1x and 2x Ls
# for i in range(1, table_size + 1):
#     L_table.set_value(1, i, i)
#     L_table.set_value(2, i, i + 1)
#
# # Runs through every dimension and calculates L value
# for i in range(3, table_size + 1):
#     for j in range(i, table_size + 1):
#         options = []
#         for k in range(i + j - 1):
#             options += L_table.find_options(i, j, k)
#         L_value = Game.mex(options)
#         L_table.set_value(i, j, L_value)
#
# end = time.time()
# print(L_table)
# print(end-start)

###############################################

# table0 = pd.read_csv("L.csv", header=None).to_numpy()
# table1 = pd.read_csv("L1.csv", header=None).to_numpy()
# for i in range(100):
#     for j in range(100):
#         assert(table0[i][j] == table1[i][j])
