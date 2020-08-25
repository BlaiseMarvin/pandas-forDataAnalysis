#Arithmetic and Data Alignment

import pandas as pd 
import numpy as np 

s1=pd.Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])

s2=pd.Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])

print(s1)
print(s2)

#Adding these together
print(s1+s2)

#for label locations that do not overlap, we have NaN introduced

#for dataframes, alignment is done for both columns and rows

df1=pd.DataFrame(np.arange(9.).reshape((3,3)),columns=list('bcd'),index=['Ohio','Texas','Colorado'])

df2=pd.DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])

print(df1)
print(df2)

#Adding these together ought to return a dataframe whose index and columns are the unions of each of the dataframes
print(df1+df2)

#Arithmetic methods with fill values
#in arithmetic operations between differently indexed objects you may want to fill a special value like 0

df1=pd.DataFrame(np.arange(12.).reshape((3,4)),columns=list('abcd'))
df2=pd.DataFrame(np.arange(20.).reshape((4,5)),columns=list('abcde'))

print(df1)
print(df2)

df2.loc[1,'b']=np.nan
print("\n")
print(df1)
print("\n")
print(df2)


print(df1+df2)
#if we use the add method, we get to fill value
z=df1.add(df2,fill_value=0)
print(z)

