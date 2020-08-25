#Work house Data Structures: DataFrame and Series
# aseries is  a one dimensional array like object containing a sequence of values
#And an assosciated array of data labels called its index
import pandas as pd 
import numpy as np 

obj=pd.Series([4,7,-5,3])
print(obj)

#To get the array representation :
print(obj.values)

#The index representation
print(obj.index)

#Let's customize our indices i.e. our lables
obj2=pd.Series([4,7,-5,3],index=['d','b','a','c'])

print(obj2)

print(obj2.index)
print(obj2.values)

#Labels can be used in the index when selecting values
print(obj2['a'])

#setting values through the index
obj2['d']=6

print(obj2)

#Accessing lot's of values using a list of indices
print(obj2[['c','a','d']])

#Filtering using Numpy's boolean indexing
print(obj2[obj2>0])

#Arithmetic operations
print(obj*2)

#Using numpy methods such as exp
expz=np.exp(obj2)
print(expz)

#Using a Series as an ordered Dict
print('b' in obj2)

print('e' in obj2)


#You can also create a series from a Python dictionary
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

#creating the series
obj3=pd.Series(sdata)

print(obj3)


#You can override the order in which the keys are stated

states=['California','Ohio','Oregon','Texas']

obj4=pd.Series(sdata,index=states)
print(obj4)

#Using the isnull and notnull to detect missing data
print(pd.isnull(obj4))

#Not null method
print(pd.notnull(obj4))

#Instead of using top level methods, series also has these instance methods
print(obj4.isnull())

print("\n")
print(obj3)
print("\n")
print(obj4)

#Series automatically aligns by index label in arithmetic operations
print("\n")
print(obj3+obj4)


#Both the series object  and its index have a name attribute, which intergrates with other key areas of pandas functionality

obj4.name='population'
obj4.index.name='state'
print(obj4)
print(obj4.index)

#A series' index can be altered in place by assignment
print(obj)

#altering the index
obj.index=['Bob','Steve','Jeff','Ryan']
print(obj)