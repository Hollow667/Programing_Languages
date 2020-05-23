from matplotlib import pyplot as plt

#set the style of the plot
#print(plt.style.available) #see all styles
styles = ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
plt.style.use(styles[2])


#add title
plt.title("Title of the polt")
plt.xlabel("x_label title")
plt.ylabel("y_label title")

#add a series
dev_x = [0, 1, 2, 3, 4, 5, 6]
dev_y = [10,12,13,1,34,45,34]
plt.bar(dev_x, dev_y, color ='k', linestyle = '--', linewidth = 3, label = "first_ser")
# k = blacb, -- = dashed line

#add second date series
dev_x = [2, 3, 4, 6, 7, 8, 10]
dev_y = [14,13,12,10,36,44,39]
plt.plot(dev_x, dev_y,color ='b', label = "second_ser")
#b = blue


#show legend (name of each seriese
plt.legend()

#show the grid
plt.grid(True)

#save the plt
plt.savefig("plot.png")

#show the polt
plt.show()



