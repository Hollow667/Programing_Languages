import pandas as pd

data = pd.read_csv('..\Data\pandas-master\pokemon_data.csv')

# add column to data
data['A+S'] = data.Attack + data.Speed
print(data.head(5))

data['Note'] = "a note"
print(data.head(5))

# get the data without specific column
new_data = data.drop(columns = ["Type 1"])
print(new_data.head(5))

# calculate the sum of each row columns (use summ(axis=1) to calculate in the x axis direction)
data['Total'] = data.iloc[:,4:10].sum(axis=1) # in x direction
print(data.head(5))

# change 'Type 1' value to 'Flame' if 'Type 1' == Fire
df1 = data.loc[data['Type 1'] == 'Fire'] # choose data
df1.loc[df1['Type 1'] == 'Fire', 'Type 1'] = 'Flame'
print(df1.head(5))

# change 'Type 1' value to 'Flame' and 'Type 2' to 'Love' if Speed > 80
df1 = data # choose data
df1.loc[df1['Speed'] > 80, ['Type 1', 'Type 2']] = ['Flame', 'Love']
print(df1.head(10))
