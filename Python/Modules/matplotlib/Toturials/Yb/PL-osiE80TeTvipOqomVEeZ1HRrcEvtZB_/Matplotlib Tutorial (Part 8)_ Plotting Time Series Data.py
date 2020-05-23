from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates


dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30),
    ]

y = [0, 1, 3, 4, 6, 5, 7]


plt.plot_date(dates, y, linestyle = 'solid')
# do not mix x labels
plt.gcf().autofmt_xdate()

# change the foramte of the date shown in x labels
date_format = mpl_dates.DateFormatter("%b, %d %y")
plt.gca().xaxis.set_major_formatter(date_format)

plt.title("Plot Title")
plt.xlabel("x_label Title")
plt.ylabel("y_label Title")
plt.legend()
plt.show()

