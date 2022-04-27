import numpy as np
import pandas as pd
from L_Dominoes import L
table_size = 40
test = L(table_size, table_size)



for i in range(1,table_size+1):
    test.set_value(1,i,i)
    test.set_value(2, i, i + 1)

for i in range(3,table_size+1):
    for j in range(i,table_size+1):
        options = []
        for k in range(i+j-1):
            options += test.find_options(i, j, k)
        l_value = test.mex(options)
        test.set_value(i, j, l_value)

test.to_dataframe().to_csv("L.csv")
