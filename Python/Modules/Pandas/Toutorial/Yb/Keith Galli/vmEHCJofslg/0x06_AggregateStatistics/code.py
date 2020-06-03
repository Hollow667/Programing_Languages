import pandas as pd

data = pd.read_csv('..\Data\pandas-master\pokemon_data.csv')

# get the mean of data sorted by (grouped by) 'Type 1' column value
# so all the columns that has the same value for 'Type 1' will be considiered one data type
print(data.groupby(['Type 1']).mean())


# get the sum of data sorted by (grouped by) 'Type 1' column value
# so all the columns that has the same value for 'Type 1' will be considiered one data type
print(data.groupby(['Type 1']).sum())


# get the count of data sorted by (grouped by) 'Type 1' column value
# so all the columns that has the same value for 'Type 1' will be considiered one data type
print(data.groupby(['Type 1']).count())

# get the count of the count column grouped by 'Type 1' column
# use this trick to calculate the NAN value rows
data['count'] = 1 # adding the 'count' column
print(data.groupby(['Type 1']).count()['count'])

# get the count of the count column grouped by 'Type 1' column and 'Type 2' column
# use this trick to calculate the NAN value rows
data['count'] = 1 # adding the 'count' column
print(data.groupby(['Type 1', 'Type 2']).count()['count'])
