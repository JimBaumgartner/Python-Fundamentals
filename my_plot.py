import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import csv
import pprint

with open('my_data.csv', newline='') as data:
    data_reader = list(csv.reader(data))


    date = data_reader[0].index('DATE')
    dpws = data_reader[0].index('DailyPeakWindSpeed')
    hdpt = data_reader[0].index('HourlyDewPointTemperature')
    
    my_date_values = []
    my_dpws_values = []
    my_hdpt_values = []
    


    for i in data_reader[1:]:
        x = datetime.strptime(i[date],'%Y-%m-%dT%X')
        try:
            wind = int(i[dpws])
            dew = int(i[hdpt])
        except Exception:
            continue

        # if not isinstance(y,int):
            # continue
        my_date_values.append(x)
        my_dpws_values.append(wind)
        my_hdpt_values.append(dew)

plt.plot(my_date_values,my_dpws_values, color='blue')
plt.plot(my_date_values,my_hdpt_values, color='green')
plt.show()
# for i in data_reader[1:]:
        #print(row)
        

# x = np.linespace(0,2,100)

# plt.plot(x, x, label="linear")
# plt.plot(x, x**2, label="quadratic")
# plt.plot(x, x**3, label="cubic")

# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title('Title level')

# plt.legend()
# plt.show()
