# I do not like this one
from matplotlib import pyplot as plt

data = [1, 2,3 ,4 ,5, 6, 7, 9, 9]

plt.hist(data, edgecolor="black")

plt.title("Plot Title")
plt.xlabel("x_label")
plt.ylabel("y_label")
plt.legend()
plt.show()
