'''get a real data'''

## get data
import pandas as pd
airports_df = pd.read_csv('Data/airports.csv', header=None, error_bad_lines=False, 
                          names=['iata', 'name', 'city', 'state', 'country', 'latitude', 'longitude'])
airports_df.dropna(inplace=True)
airports_df.drop_duplicates(inplace=True)
# split data into features and labels
x = airports_df.loc[:,['iata', 'name', 'city', 'country', 'latitude', 'longitude']]
y = airports_df.loc[:,['state']]


# Split into test and training data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.9, random_state=42)
print("x train data: " , x_train.shape)
print("x test data: ", x_test.shape)
print("y train data: " , y_train.shape)
print("y test data: ", y_test.shape)
