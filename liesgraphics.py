import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt


df = pd.read_csv("trump_lies.csv")

df['month'] = pd.DatetimeIndex(df["date"]).month


result = df["month"].value_counts()

a = dict(result)
keys = a.keys()
values = a.values()

fig = plt.figure()
fig.suptitle("Trump's Lies Graphics of 2017 months")
plt.ylabel("Number of lies")
plt.xlabel("Month of 2017")
plt.bar(keys,values)
plt.show()
