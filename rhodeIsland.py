import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# importing data and cleaning!
filePath = input('Masukkan file path: ')
rhodeIsland = pd.read_csv(filePath, low_memory=False)
rhodeIsland = rhodeIsland[:20000]
print(rhodeIsland.shape)
dateTime = rhodeIsland['date'].str.cat(rhodeIsland['time'], sep=' ')
rhodeIsland['dateTime'] = pd.to_datetime(dateTime)
rhodeIsland.set_index('dateTime', inplace=True)
columnsDrop = ['raw_row_number', 'date', 'time',]
rhodeIsland.drop(columnsDrop, axis='columns', inplace=True)
print(rhodeIsland.head())
rhodeIsland.dropna(subset=['outcome', 'arrest_made', 'subject_race', 'subject_sex',], inplace=True)
missingValues = rhodeIsland.isnull().sum()
filteringNan = (missingValues>=18000) & (missingValues<=rhodeIsland.shape[0])
columns = rhodeIsland.columns
rhodeIsland = rhodeIsland[columns[~filteringNan]]
print(rhodeIsland.head())
boolColumn = ['arrest_made', 'citation_issued', 'warning_issued', 'frisk_performed', 'search_conducted']
for column in boolColumn:
    rhodeIsland[column] = rhodeIsland[column].astype('bool')
columns = rhodeIsland.columns
raceSex = ['subject_race', 'subject_sex', 'outcome']
for index in raceSex:
    print("\ncolumn's name: {}".format(index))
    print(rhodeIsland[index].value_counts(dropna=False))
# Filtering!    
blackFemale = (rhodeIsland['subject_sex']=='female') & (rhodeIsland['subject_race']=='black')
whiteFemale = (rhodeIsland['subject_sex']=='female') & (rhodeIsland['subject_race']=='white')
femaleBlack = rhodeIsland[blackFemale]['outcome'].value_counts(normalize=True)
femaleWhite = rhodeIsland[whiteFemale]['outcome'].value_counts(normalize=True)
# Generate 'Outcome'
blackMale = (rhodeIsland['subject_sex']=='male') & (rhodeIsland['subject_race']=='black')
whiteMale = (rhodeIsland['subject_sex']=='male') & (rhodeIsland['subject_race']=='white')
maleBlack = rhodeIsland[blackMale]['outcome'].value_counts(normalize=True)
maleWhite = rhodeIsland[whiteMale]['outcome'].value_counts(normalize=True)
xLabel = np.arange(len(femaleBlack.index))
labelText = []; listLabel = list(femaleWhite.index)
for index in range(len(listLabel)):
    text = str.capitalize(listLabel[index])
    labelText.append(text)
lebar = 0.15
fig, axs = plt.subplots()
axs.bar(xLabel - lebar*3/2, femaleBlack, width=lebar, label="Black Female")
axs.bar(xLabel - lebar/2, femaleWhite, width=lebar, label="White Female")
axs.bar(xLabel + lebar/2, maleBlack, width=lebar, label="Black Male")
axs.bar(xLabel + lebar*3/2, maleWhite, width=lebar, label="White Male")
axs.set_ylabel('Percentage')
axs.set_xlabel('Outcome')
axs.set_title('Gender & Race vs Outcome')
axs.set_xticks(xLabel)
axs.set_xticklabels(labelText); plt.legend()
axs.grid(color='black', linestyle='--')
plt.show()
