import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# Reading the csv file as a dataframe
df1 = pd.read_csv('Economically-active-qualification-borough.csv', encoding='UTF-8')

# Omitting rows with missing values
df = df1.dropna()

# Omitted nominal attributes
del df['Area']

# Extracting the values
rates = df.values

# Clustering
k_means = KMeans(n_clusters = 5, init = 'random') # with 5 clusters
k_means.fit(rates)
df['Five clusters'] = pd.Series(k_means.predict(df.values), index = df.index)
sns.pairplot(df, hue = 'Five clusters')

plt.show()

