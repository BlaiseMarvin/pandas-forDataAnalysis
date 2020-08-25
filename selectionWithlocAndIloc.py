#To index,in dataframes, along the rows, we use loc and iloc
import pandas as pd 
import numpy as np 

#loc and iloc, enable you to select a subset of rows and columns from a dataframe, with numpy like notation,
#using either axis labels (loc) or integers(iloc)

#as an example, let's select a single row and multiple columns by label

data=pd.DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
print(data)

print(data.loc['Colorado',['two','three']])
#selects Colorado by index, i.e. by index it selects the row named Colorado
#it then after selects two columns named two and three

#iloc on the other hand selects by integer
print(data.iloc[2,[3,0,1]])

#selecting rows and columns by index

#selecting a single row
print(data.iloc[2])


#iloc extra
print(data.iloc[[1,2],[3,0,1]])


#both indexing functions, work with slices
print(data.loc[:'Utah','two'])


#combination of iloc and boolean indexing
print("\n")
print(data)
print(data.iloc[:,:3][data['three']>5])
