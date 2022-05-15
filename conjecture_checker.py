import pandas as pd
table = pd.read_csv("L.csv", header=None).to_numpy()
print(table)
for i in range (1,249, 2):
    print(i+1,table[i][i])