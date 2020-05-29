import pandas as pd
airports_df = pd.read_csv('Data/airports.csv', header=None, error_bad_lines=False, 
                          names=['iata', 'name', 'city', 'state', 'country', 'latitude', 'longitude'])

#Use info to check for missing values
print(airports_df.info())

#Use dropna to remove rows missing values
airports_no_nulls_df = airports_df.dropna()

#Specify inplace=Tru to update the existing DataFrame
airports_df.dropna(inplace=True)

#If you get date from multiple sources you can indicate if there is miltiple rows
print(airports_df.duplicated())

#Merge rows and remove duplicated rows
airports_no_duplicates_df = airports_df.drop_duplicates()
airports_df.drop_duplicates(inplace=True)

