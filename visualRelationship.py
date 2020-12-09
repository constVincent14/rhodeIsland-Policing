import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
filePath = input("Masukkan file path: ")
# importing files:
rhodeIsland = pd.read_csv(filePath, index_col='dateTime')
rhodeIsland.index = pd.to_datetime(rhodeIsland.index)
columns = rhodeIsland.columns
print(rhodeIsland.index.dtype, columns, sep="\n")
for column in columns:
    print("\nColumn name: {}".format(column))
    print(rhodeIsland[column].unique())
groupByHours = rhodeIsland.groupby(rhodeIsland.index.hour)['search_conducted'].mean()
print(groupByHours.head())
xLabel = np.arange(len(rhodeIsland.index.hour.unique())) * 2
labelText = []; listLabel = list(groupByHours.index)
for index in range(len(listLabel)):
    text = str(listLabel[index]) + ':00'
    labelText.append(text)
# APAKAH POLISI CENDERUNG: SEARCH_CONDUCTED PADA MALAM HARI?
plt.plot(xLabel, groupByHours, label='Search Conducted', color='red')
plt.xlabel('Time (hour)')
plt.ylabel('Probability')
plt.title('Search Conducted vs. Time')
plt.xticks(xLabel, labels=labelText, rotation=90)
plt.legend()
plt.grid(color='blue', linestyle='--')
plt.show()
# APAKAH KASUS SPEEDING SERING TERJADI DI MALAM HARI?
reasonSpeeding = rhodeIsland[rhodeIsland['reason_for_stop']=='Speeding']
speedingHours = reasonSpeeding.groupby(reasonSpeeding.index.hour)['reason_for_stop'].count()
plt.plot(xLabel, speedingHours, label='Speeding', color='blue')
plt.ylabel('Total Cases')
plt.xlabel('Time (hour)')
plt.title('Speeding cases vs. Time')
plt.xticks(xLabel, labels=labelText, rotation=90)
plt.legend()
plt.grid(color='gray', linestyle='--')
plt.show()
