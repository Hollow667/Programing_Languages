'''get real data'''
'''
file=open('Data/data.csv','w')

for i in range(1000):
	file.write(str(i)+","+str(i*i-i)+'\n')
file.close()
'''

## get data
import pandas as pd
data_df = pd.read_csv('Data/data.csv', header=None, error_bad_lines=False, 
                          names=['i', 'i*i-i'])
data_df.dropna(inplace=True)
data_df.drop_duplicates(inplace=True)
# split data into features and labels
x = data_df.loc[:,['i']]
y = data_df.loc[:,['i*i-i']]
print(data_df)

# Split into test and training data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.9, random_state=42)
print("x train data: " , x_train.shape)
print("x test data: ", x_test.shape)
print("y train data: " , y_train.shape)
print("y test data: ", y_test.shape)

## Train the model
from sklearn.linear_model import LinearRegression
# Create an instance of the class
regressor = LinearRegression()

# Use the fit ,ethod to train the model using your training data
regressor.fit(x_train, y_train)

# Predict returns the values the trained model prodect for new data
y_pred = regressor.predict(x_test)

# Test
for i in range(10):
    print(i,x_test.iloc[i,0], y_test.iloc[i,0], y_pred[i][0])

file=open("y_pred_df.csv", "w")
for i in range(y_test.shape[0]):
    print(str(x_test.iloc[i,0]), "," , str(y_pred[i][0]) + "," + str(y_test.iloc[i,0]), file=file)
file.close()
    
# note y_pred is a numpy array not a pandas object
# to transfer it use
y_pred_df = pd.DataFrame(y_pred)
print(y_pred_df.head(10))

## Evaluating Accuracy of A Model Using Calculations
#Mean Squared Error (MSE) is the average error
from sklearn import metrics
MSE = metrics.mean_squared_error(y_test, y_pred)
print(MSE)

#Root Mean Squarred Error (RMSE) is the square root of the mean squared error
# RMSE = sqrt(MSE)
RMSE = MSE**0.5
print(RMSE)
