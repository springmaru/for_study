#import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import csv
from statsmodels.tsa.arima_model import ARIMA
import pandas as pd

f = open('rubhistory.csv', 'r', encoding = 'utf-8')
rdr = csv.reader(f)
#주 기준으로 넣자. 0주부터 시작 !
value_list = []
key_list = []


for line in rdr:
    key_list.append(list(line)[1])
    value_list.append(list(line)[1])


value_list = list(map(float, value_list[1:]))
value_list = value_list[:-12]
key_list = key_list[:-12]



#plt.plot(list(range(1,len(value_list)+1)),value_list)


csv_reading_demo = pd.read_csv("rubhistory.csv",parse_dates=['Date'], index_col = 'Date')
print(csv_reading_demo)
#plt.plot(list(range(1,len(before_war)+1)),before_war)

#plt.plot(list(range(1,len(after_war)+1)),after_war)

csv_reading_demo.plot()
plt.show()




f.close()