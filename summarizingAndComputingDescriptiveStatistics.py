#consider a small dataframe
import pandas as pd 
import numpy as np 

df=pd.DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])
print(df)

#Calling a dataframe's sum method basically returns a series containing column sums
print(df.sum())

#provides the sum of values in columns 

#NA values are excluded unless the entire slice(row or column in this case is NA)
#this can be disabled using the skipna option

print("\n")
print(df)
print("\n")
print(df.mean(axis=1,skipna=False))

#some methods like idmax and idmin, return indirect statistics like the index value, where the minimum or maximum values are attained

print(df)
print("\n")
print(df.idxmax(axis=0))
print(df.idxmin(axis=0))

#the describe method
print(df.describe())

#on non numeric data
obj=pd.Series(['a','a','b','c']*4)
print(obj.describe())
