import pandas as pd
airports_df = pd.read_csv('Data/airports.csv', header=None, error_bad_lines=False, 
                          names=['iata', 'name', 'city', 'state', 'country', 'latitude', 'longitude'])

#drop deletes columns from a DataFrame
new_df = airports_df.drop(columns=['state', 'latitude', 'longitude'])
print(new_df)

#Use inplace to edit the existing DataFrame
new_df.drop(columns=['iata'], inplace=True) # will remove 'iata' from the DataFrame
print(new_df)

#Create a slice of the DataFrame and assign it to a new DataFrame
location = new_df.loc[:,['city','country']]
print(location)
