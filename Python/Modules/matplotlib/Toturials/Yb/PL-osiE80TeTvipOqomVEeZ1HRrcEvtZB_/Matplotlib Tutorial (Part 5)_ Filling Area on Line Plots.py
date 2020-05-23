from matplotlib import pyplot as plt

x_vals = [1, 2, 3, 4, 5, 6]
y_vals = [10 , 20, 23, 25, 43, 20]

plt.plot(x_vals, y_vals, color="blue", label = "first_ser")

plt.fill_between(x_vals, y_vals, alpha=0.25)

plt.legend()

plt.xlabel("x_label")
plt.ylabel("y_label")

plt.show()
