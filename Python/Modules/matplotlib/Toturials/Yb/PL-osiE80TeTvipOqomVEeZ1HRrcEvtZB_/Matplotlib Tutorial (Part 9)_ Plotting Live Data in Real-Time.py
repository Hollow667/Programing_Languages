import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_vals = []
y_vals = []
i = 0

#add new point here
def animate(k):
    global i
    x_vals.append(i)
    y_vals.append(i ** 5)

    #clear the plot then add the new values
    plt.cla()
    plt.plot(x_vals, y_vals)
    i = i + 1

#setting timer for adding the new points
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
