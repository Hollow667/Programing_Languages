import pandas as ps

## Create a new Series
airports = ps.Series([
    'Seattle-Tacoma',
    'Dulles',
    'London Heathrow',
    'Schiphol'
    ])

# Access similar to a list
print(airports[1])

# Use a loop to iterate through all the values
for value in airports:
    print(value)

## Createa a DataFrame
airports = ps.DataFrame([
    ['Seattle-Tacoma', 'Seattle', 'USA' ],
    ['Dulles', 'Washington', 'USA' ],
    ['London Heathrow', 'London', 'United Kingdom' ],
    ['Schiphol', 'Amsterdam', 'Netherlands']],
    columns= ['Name', 'City', 'Country'])
print(airports)
    

## Examining pandas DataFrame contents
#head - first n rows
print(airports.head(3))

#tail - last n rows
print(airports.tail(3))

#shape - number of rows and columns
print(airports.shape) # (4, 3)

#info will return more detailed information
print(airports.info())

## Query aDataFrame
#Request a single column
print(airports['City'])

#Request a list of columns
print(airports[['City', 'Country']])

#iloc returns specific rows and columns by position
print(airports.iloc[0,0])

#The range : returns all rows or columns
print(airports.iloc[:,:])

#You can request a range of rows or columns
print(airports.iloc[0:2,:])
print(airports.iloc[:,0:2])

#Request a list of rows or columns
print(airports.iloc[:,[0,2]]) # return first and third columns
print(airports.iloc[[0,2],[:]]) # return first and third rows
print(airports.loc[:,['Name', 'Country']]) # returns all the rows of the columns named Name amd Country















