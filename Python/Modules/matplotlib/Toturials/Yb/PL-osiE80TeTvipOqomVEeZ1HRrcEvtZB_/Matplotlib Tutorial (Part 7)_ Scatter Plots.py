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
dev_x = [10, 100, 200, 378, 456, 567, 646]
dev_y = [1045,1267,1357,1876,3445,3445,3498]
colors = [1, 3, 3, 4, 5, 6, 7]
sizes = [100, 300, 300, 400, 500, 600, 700] 
plt.scatter(dev_x, dev_y,  label = "first_ser", s=sizes, marker="o", c=colors,
            edgecolor="black", linewidth=1, alpha=0.75, cmap="Greens")
cbar = plt.colorbar()
cbar.set_label("cbar_title")

# change the scale to log
plt.xscale('log')
plt.yscale('log')

#show legend (name of each seriese
plt.legend()

#show the grid
plt.grid(True)

#save the plt
plt.savefig("plot.png")

#show the polt
plt.show()



