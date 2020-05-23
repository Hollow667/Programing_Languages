from matplotlib import pyplot as plt

fcg, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
# in the code we defined to have 2 chars: nrows = 2 and ncols = 1
# to share the x axes used sharex , you can do the same for y : sharey

x_vals = [1, 2, 3, 4, 5]
y_vals = [1, 2, 3, 4, 5]
y2_vals= [1, 2, 3, 4, 5]

ax1.plot(x_vals, y_vals)

ax1.set_title("Title1_1")
ax1.set_ylabel("y_label")

ax2.plot(x_vals, y2_vals)

ax2.set_xlabel("x_label")
ax2.set_ylabel("y_label")


#to make another plot
fcg2, ax = plt.subplots()
# in the code we defined to have 2 chars: nrows = 2 and ncols = 1
# to share the x axes used sharex , you can do the same for y : sharey

x_vals = [1, 2, 3, 4, 5]
y_vals = [1, 2, 3, 4, 5]

ax.plot(x_vals, y_vals)
ax.set_title("Title1_1")
ax.set_xlabel("x_label")
ax.set_ylabel("y_label")


plt.show()

