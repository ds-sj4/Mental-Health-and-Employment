import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Reading the csv file as a dataframe
df1 = pd.read_csv('mental-health-common-problems-borough.csv', encoding='UTF-8')

# Deleting unwanted rows
df = df1.drop(df1.index[32:])

# Deleting unwanted columns
del df['Code']
del df['Population 16-74']
del df['Panic disorder-Estimated cases']
del df['Obsessive compulsive disorder-Estimated cases']
del df['Mixed anxiety depression-Estimated cases']
del df['Generalised anxiety disorder-Estimated cases']
del df['Depressive episode-Estimated cases']
del df['All phobias-Estimated cases']
del df['Any neurotic disorder-Estimated cases']
del df['Area']

# Renaming column headings
df.rename(columns={'Any neurotic disorder-Rates per 1000 population': 'Any neurotic disorder', 'All phobias-Rates per 1000 population': 'All phobias', 'Depressive episode-Rates per 1000 population': 'Depression', 'Generalised anxiety disorder-Rates per 1000 population': 'Anxiety disorder', 'Mixed anxiety depression-Rates per 1000 population': 'Anxiety & Depression', 'Obsessive compulsive disorder-Rates per 1000 population': 'OCD', 'Panic disorder-Rates per 1000 population': 'Panic disorder'}, inplace=True)

# Changing string to numeric
df["Any neurotic disorder"] = pd.to_numeric(df["Any neurotic disorder"])
df["All phobias"] = pd.to_numeric(df["All phobias"])
df["Depression"] = pd.to_numeric(df["Depression"])
df["Anxiety disorder"] = pd.to_numeric(df["Anxiety disorder"])
df["Anxiety & Depression"] = pd.to_numeric(df["Anxiety & Depression"])
df["OCD"] = pd.to_numeric(df["OCD"])
df["Panic disorder"] = pd.to_numeric(df["Panic disorder"])

# Correlations
correl = df.corr(method = 'pearson')
print(correl)

# Normalising data
# df =  pd.DataFrame(MinMaxScaler().fit_transform(df[['Any neurotic disorder', 'All phobias', 'Depression', 'Anxiety disorder', 'Anxiety & Depression', 'OCD', 'Panic disorder']]))
# df.columns = ['Any neurotic disorder', 'All phobias', 'Depression', 'Anxiety disorder', 'Anxiety & Depression', 'OCD', 'Panic disorder']

# Wide to long
# df_long = df.melt()

# Violin Plot for the different mental health disorders in all of London
# sns.violinplot(data = df_long, x = 'variable', y = 'value') 

# Creating scatter plots for all mental disorders
sns.pairplot(df) 
plt.show()

# Extracting the values
# rates = df.values

# Clustering
# k_means = KMeans(n_clusters = 5, init = 'random') # with 5 clusters
# k_means.fit(rates)
# k_means.labels_
# df['Five clusters'] = pd.Series(k_means.predict(df.values), index = df.index)
# sns.pairplot(df, hue = 'Five clusters')


