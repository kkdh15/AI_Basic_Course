import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('darkgrid')

figure = plt.figure(figsize=(15,5))
axes1 = figure.add_subplot(1,2,1)
axes2 = figure.add_subplot(1,2,2)

sns.regplot(x='fare',y='survived',data=titanic,ax=axes1)
sns.regplot(x='age',y='fare',data=titanic,ax=axes2)

plt.show()