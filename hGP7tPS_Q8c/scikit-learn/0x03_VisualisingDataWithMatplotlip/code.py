## using matplotlib to draw graohs
from matplotlib import pyplot as plt

# create plots directly from the DataFrame
import pandas as pd
data_def = pd.read_csv('Data/y_pred_df.csv')
#first column is x_test, second is y_pred, y_test
dev_x = data_def.iloc[:,0].to_list()
dev_y_pred = data_def.iloc[:,1].to_list()
dev_y_test = data_def.iloc[:,2].to_list()

# You can draw a line graph to show the predicted va;ues of trained model
plt.plot(dev_x, dev_y_pred, color ='black', linestyle = '--', linewidth = 0.5,  marker = '.',  label = "y_pred")

# Show the test (original) data
plt.plot(dev_x, dev_y_test, color ='blue', linestyle = "", linewidth = 0.5,  marker = '.',label = "y_test")

#
plt.grid(True)
plt.legend()
plt.show()

