import pandas as pd 
import numpy as np 

obj=pd.Series(np.arange(5.),index=['a','b','c','d','e'])
print(obj)

#dropping stuff returns a new object
new_obj=obj.drop('c')

print(new_obj)

#dropping by lists
new_obj1=obj.drop(['d','c'])
print(new_obj1)


#with series, we can only delete by index

#with dataframes,we can delete data from either axis
#to illustrate, let's create an example DataFrame

data=pd.DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
print("\n")
print(data)

#Calling drop, with a sequence of labels, drops from the row axis, axis 0
new_obj=data.drop(['Colorado','Ohio'])
print("\n")
print(new_obj)

#Dropping by the columns
new_obj=data.drop('two',axis=1)
print("\n")
print(new_obj)

#instead of always returning a new object, we can modify inplace
print(obj)
obj.drop('c',inplace=True)
print(obj)