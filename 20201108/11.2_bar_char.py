import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("./move.xlsx")
df = df.replace('-',0)

df_seoul = df.iloc[2]
seoul_labels = df_seoul.index[2:]
seoul_means = df_seoul.values[2:]

df_busan = df.iloc[3]
busan_means = df_busan.values[2:]

labels = ['G1','G2','G3','G4','G5']
men_means = [20,34,30,35,27]
women_means = [25,32,34,20,25]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label = 'Seoul')
rects2 = ax.bar(x + width/2, women_means, width, label = 'Busan')

ax.set_ylabel('People')
ax.set_title('Seoul,Busan In/Out')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()