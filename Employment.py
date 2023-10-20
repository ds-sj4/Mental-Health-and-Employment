import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Reading the csv file as a dataframe
df2 = pd.read_csv('london-jobs-history-borough-2010.csv', encoding='UTF-8')

# Deleting unwanted rows
df1 = df2.drop(df2.index[32:])

# Filtering data
df = df1.filter(['Area','2006'])

# Plotting data

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Setting axes
Boroughs = df['Area']
y_pos = np.arange(len(Boroughs))
Employment = df['2006']
error = np.random.rand(len(Boroughs))

ax.barh(y_pos, Employment, xerr = error, align = 'center')
ax.set_yticks(y_pos, labels = Boroughs)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Employment')
ax.set_title('Employment Rates in London')
plt.show()

