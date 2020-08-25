import pandas as pd 
import numpy as np 

ser=pd.Series(np.arange(3.))
print(ser)
#print(ser[-1]), this results in an error, pandas confuses this index with the actual index

ser2 = pd.Series(np.arange(3.),index=['a','b','c'])
print(ser2)
print(ser2[-1])

#if your index axis is made up of integers, then indexing directly with integers is tricky, you should basically employ loc and iloc

