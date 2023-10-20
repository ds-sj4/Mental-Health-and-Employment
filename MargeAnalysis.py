import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Reading the employment csv file as a dataframe
df2 = pd.read_csv('london-jobs-history-borough-2010.csv', encoding='UTF-8')

# Deleting unwanted rows
df1 = df2.drop(df2.index[32:])

# Filtering data
df_employ = df1.filter(['Area','2006'])

# Reading the mental health csv file as a dataframe
df_mh = pd.read_csv('Mental_Health_Borough.csv', encoding='UTF-8')

# Renaming columns
df_employ.rename(columns = {'2006': 'Employment Rate'}, inplace = True)

# Merging dataframes
df = pd.merge(df_employ, df_mh, how='inner', on = 'Area')

# Export to csv file
df.to_csv('C:/Users/sarah/OneDrive/Documents/BDS/Foundation of Data Analytics/Project/Data/Analysis.csv', encoding='utf-8', index = False)

