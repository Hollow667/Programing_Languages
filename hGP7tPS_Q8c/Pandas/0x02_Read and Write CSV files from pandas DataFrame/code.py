import pandas as pd
## read_csv loads a DataFrame from a CSV
airports_df = pd.read_csv('Data/airports.csv')
print(airports_df)

#Rows with an extra , or other issues cause an error and the file does not load
#Specify error_bab_lines=False to skip rows with errors
airports_df = pd.read_csv('Data/airports.csv', error_bad_lines=False)
print(airports_df)
#Missing values appear as NaN

#if the first row does not contain column headers specify header=None
airports_df = pd.read_csv('Data/airports.csv', header=None)
print(airports_df)

#Provide names for the columns with the names parameter
airports_df = pd.read_csv('Data/airports.csv', header=None,
                          names=['iata', 'name', 'city', 'state', 'country', 'latitude', 'longitude'])
print(airports_df)

## Use to_csv to write the contents of a DataFrame to a CSV file
#Specify index=False if you do not want to include the index column
airports_df.to_csv('Data/MyNewCSVFile.csv', index=False)
