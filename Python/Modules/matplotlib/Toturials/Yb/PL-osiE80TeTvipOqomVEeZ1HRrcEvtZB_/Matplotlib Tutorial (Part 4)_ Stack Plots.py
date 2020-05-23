from matplotlib import pyplot as plt

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 4, 4, 3, 2, 2, 5]
player2 = [1, 2, 2, 3, 3, 3, 4, 4, 5]
player3 = [5, 3, 4, 3, 2, 1, 2, 2, 3]

labels = ["Player1", "Player2", "Player3"]
colors = ["green", "red", "blue"]

plt.stackplot(minutes, player1, player2, player3, labels = labels, colors = colors)

plt.title("Plot Title")

plt.legend(loc=(0.07, 0.05)) # 0.07 = 7% to the left, 5% to above, you can use loc="upper left" 

plt.tight_layout()
plt.show()
