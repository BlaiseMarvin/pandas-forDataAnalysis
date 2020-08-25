import pandas as pd 
import numpy as np 

#another class of related methods extracts information about the values contained in a one dimensional series
obj=pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

#first function is unique, which gives you an array of unique values in a Series
uniques=obj.unique()
print(uniques)

#to sort, use the uniques.sort()

#Relatadely, value_counts, computes a series containing value frequencies
print("\n")
print(obj)
print("\n")
print(obj.value_counts())

#the is in method
print("\n")
print(obj)
 
mask = obj.isin(['b','c'])
print(mask)

print(obj[mask])