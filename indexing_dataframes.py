#Indexing a dataframe is for retrieving one or more columns, either with a single value or sequence

import pandas as pd 
import numpy as np 

data=pd.DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
print(data)

#indexing now just gives columns
print(data['two'])

#getting two columns
print(data[['three','one']])

#Indexing, like this has a few special cases
# a few special cases now
print(data[:2]) #this slices by the row

#Boolean indexing
print(data[data['three']>5])

#The row selection syntax is provided as a convinience [:2]
#Passing a single element, or list to [] with dataframes, ends up selecting a column instead

#another use case is indexing with boolean
print(data<5)

#setting stuff, using boolean indexing
data[data<5]=0
print(data)