from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = [12,45,36,67,24,47]
labels=["1", "2", "3", "4", "5", "6"]
explode = [0,0,0.1,0,0,0]
#colors = ["red", "yellow", "blur", "orange", "pink", "green"] # colors = colors
plt.pie(data, labels = labels, wedgeprops={'edgecolor' : 'black'},
        explode = explode, shadow = True, startangle=90, autopct = "%1.1f%%")

cbar = plt.colorbar()
cbar.set_label("cbar_title")

plt.title("Plot Title")
plt.tight_layout()
plt.show()
