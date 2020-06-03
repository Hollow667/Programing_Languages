import pandas as pd

data = pd.read_csv('..\Data\pandas-master\pokemon_data.csv')

# show data the its Type 1 == Grass and its Type 2 == Poison
df1 = data.loc[(data['Type 1'] == 'Grass') & (data['Type 2'] == 'Poison')]
print(df1.head(5))

# show data the its Type 1 == Grass or its Type 2 == Poison
df1 = data.loc[(data['Type 1'] == 'Grass') | (data['Type 2'] == 'Poison')]
print(df1.head(5))


# show data the its Type 1 == Grass and its Type 2 == Poison and HP > 70
df1 = data.loc[(data['Type 1'] == 'Grass') & (data['Type 2'] == 'Poison') & (data['HP']>70)]
print(df1.head(5))

# show data that its value in 'Name' column contains the string 'Mega'
df1 = data.loc[data['Name'].str.contains('Mega')]
print(df1.head(5))

# show data that its value in 'Name' column DOES NOT contains the string 'Mega'
df1 = data.loc[~data['Name'].str.contains('Mega')]
print(df1.head(5))

# to seave results after filtering use
#df1.reset_index(drop=true, inplace=True)
#df1.to_csv("filtered.csv")
