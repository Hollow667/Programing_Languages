import pandas as pd

# get specific size of data 
data = pd.read_csv('..\Data\pandas-master\pokemon_data.csv', chunksize=5)

for row in data:
    print(row)
