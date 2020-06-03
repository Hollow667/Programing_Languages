import pandas as pd

data = pd.read_csv('..\Data\pandas-master\pokemon_data.csv')

# to csv file
data.to_csv("pokemon_data.csv")

# to csv without indexes
data.to_csv("pokemon_data__no_index.csv", index = False)

# to excel
#data.to_excel("pokemon_data.xlsx")

# to excel without indexes
#data.to_excel("pokemon_data__no_index.xlsx")

# to txt file and seperate it by tabs
data.to_csv("pokemon_data.txt", index=False, sep='\t')
