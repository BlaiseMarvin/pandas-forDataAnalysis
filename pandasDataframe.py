#A dataframe represents a rectangular table of data and contains an ordered collection
#of columns, each of which can be of different value: numeric, string, boolean, etc
#Dataframe has both row and column index, 
#many ways to construct a dataframe,most common one is from a dict of equal length lists
#or from numpy arrays

import pandas as pd 
import numpy as np
data={
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
    'year':[2000,2001,2002,2001,2002,2003],
    'pop':[1.5,1.7,3.6,2.4,2.9,3.2]
}

frame=pd.DataFrame(data)
print(frame)

#For large data frames, the head method, selects the first 5 rows
print(frame.head())

#Specifying your own custom sequence of columns arrangement
column_seq=['year','pop','state']
frame_mod=pd.DataFrame(data,columns=column_seq)
print(frame_mod)

#Passing a column, that isn't among the already named columns, returns NaN

frame2=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
print(frame2)
print(frame2.columns)

#A column can be retrived either by dict like notation or by attribute
print(frame['state'])

#attribute
print(frame.year)

#The returned series has the same index as the DataFrame and their name attribute has been appropriately set

#Rows can be retrieved by: position, or name, with the special loc attribute
print("\n")
print(frame2)
#Retrieving 
print("\n")
print(frame2.loc['three'])

#We can modify columns by assignment
#The empty debt column, can be assigned to a scalar value, or to an array of values
frame2['debt']=16.5
print(frame2)

#or we can modify a column and assign it an array
frame2['debt']=np.arange(6.)
print(frame2)

#When assigning an array, it's length must match with the dataframe's length.
#that's what you consider when assigning an array

#Now when assigning a Series, to a column, Pandas will fill out the data in those holes, with the corresponding index values

val = pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
print(frame2)

#Assigning a column, that doesn't exist will create a new column
#The del keyword, will delete columns as with a dict

#Let's first add a boolean column
frame2['eastern']=frame2.state=='Ohio'
print(frame2)

#Now deleting the column
del frame2['eastern']

print(frame2)

#The column is a view on the DataFrame, to use a copy, always use the .copy() method

#Another common form of data is a nested dict of dicts
pop = {
    'Nevada':{2001:2.4,2002:2.9},
    'Ohio':{2000:1.5,2001:1.7,2002:3.6}
}

#In a nested dictionary, the outer keys are the columns,
#Inner keys are the row indices
frame3=pd.DataFrame(pop)
print(frame3)

#You can transpose a DataFrame
print(frame3.T)

#sorting the index to what you want
zx=pd.DataFrame(pop,index=[2001,2002,2003])
print(zx)

#
print(frame3['Ohio'][:1])

#Setting the index and columns attribute names
print(frame3)
frame3.index.name='year'
frame3.columns.name='state'

print(frame3.values)

#The data is returned as a 2D array

