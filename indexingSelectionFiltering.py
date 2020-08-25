#Indexing, Selection and Filtering
#series indexing works analogously to numpy's array indexing, except that we can actually use the index value to index with series

import pandas as pd 
import numpy as np 

obj=pd.Series(np.arange(4.),index=['a','b','c','d'])
print(obj)

print(obj['b']) #indexing with the actual value of the index.

#we can also index with numbers
print(obj[1])

print(obj[2:4])

# we can also pass a list.
print(obj[['b','a','d']])

print(obj[[1,3]])

print(obj[obj<2])

#Slicing with labels behaves differently, in that the end point is inclusive
print(obj['b':'c'])