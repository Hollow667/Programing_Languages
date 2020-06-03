import pandas as pd

# csv files seperated by ,
data = pd.read_csv('..\Data\pandas-master\pokemon_data.csv')

# excel files
# data = pd.read_excel('..\Data\pandas-master\pokemon_data.xlsx')

# txt files deperated by tabs
data = pd.read_csv('..\Data\pandas-master\pokemon_data.txt', delimiter = '\t')

# show data
print(data)

# show first 5
print(data.head(5))

# show last 5
print(data.tail(5))

# show columns names
print(data.columns)

# show a specific column
print(data['Name'])

print(data[['Name', 'Type 1']])

# show first row and all columns
print(data.iloc[1,:])

# show rows 4 -> 7 and all columns
print(data.iloc[4:8,:])

# show rows 2 -> 5 and columns 1 -> 4
print(data.iloc[2:6, 1:5])

# iterate through each row
'''
for index, row in data.iterrows():
    print(index, row)

for index, row in data.iterrows():
    print(index, row['Name']) # 'Name' is one of the columns names    
'''

# print data with specific conditions
print(data.loc[data["Type 1"] == "Fire"])
