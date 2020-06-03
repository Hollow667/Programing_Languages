import pandas as pd

data = pd.read_csv('..\Data\pandas-master\pokemon_data.csv')

# get max min std count
print(data.describe())

# sort by specific column
print(data.sort_values('Name')) # by the column called Name
print(data.sort_values('Name', ascending = False)) # sort in reverse
print(data.sort_values(['Type 1', 'HP'])) # sort by the column 'Type 1' then 'HP'


