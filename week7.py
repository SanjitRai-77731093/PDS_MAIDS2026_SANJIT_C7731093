import warnings

import pandas as pd
import numpy as np
import seaborn as sns
from pandas._libs import pandas_datetime

warnings.filterwarnings('ignore')
# using list
product_data=[['e-book', 2000], ['plants', 6000], ['Pencil', 3000]]
#2d list, similar to 2d array

indexes=[1,2,3]

columns_name=['product', 'unit_sold']
product_df = pd.DataFrame(data=product_data, index=indexes,
columns=columns_name)
print(product_df)

# using dictionaries
product_data={'product': ['e-book', 'plants', 'Pencil'], 'unit_sold':
[2000, 5000, 3000]}
product_df = pd.DataFrame(data=product_data)
print(product_df)

# using numpy array
products = np.array([['','product','unit_sold'], [1, 'E-book',2000],
[2, 'Plants', 6000], [3, 'Pencil', 3000]])
product_pf = pd.DataFrame(data=products[1:,1:],index=products[1:,0 ],
columns=products[0,1:])
print(product_pf) # output is same as of first case

df = pd.read_csv('data/dirtydata.csv')
print(df.head(10))

#Print information about the data:
print(df.info())
print(df.isna().sum())
print(df.duplicated())

df = pd.read_csv('data/dirtydata.csv')
new_df = df.dropna()
print(new_df.to_string())

df = pd.read_csv('data/dirtydata.csv')
df.fillna(130)
print(new_df.to_string())

df = pd.read_csv('data/dirtydata.csv')
df["Calories"].fillna(130)

df = pd.read_csv('data/dirtydata.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)

df = pd.read_csv('data/dirtydata.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)

df = pd.read_csv('data/dirtydata.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)

df = pd.read_csv('data/dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())

df.dropna(subset=['Date'], inplace = True)

df.loc[7, 'Duration'] = 45

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace = True)

print(df.duplicated())

df.drop_duplicates(inplace = True)
