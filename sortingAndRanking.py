#sorting and ranking
# to sort lexicographically, we use the sort_index method which returns a new object
import pandas as pd 
import numpy as np 

obj=pd.Series(range(4),index=['d','a','b','c'])
print(obj)
print("\n")

print(obj.sort_index()) #this sorts the indices

#with a dataframe, you can sort by index on either axis
frame=pd.DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],columns=['d','a','b','c'])
print("\n")
print(frame)
print("\n")
print(frame.sort_index()) # it originally sorts the row index

#sorting the column index
print(frame.sort_index(axis=1))

#by default, the data is sorted in ascending order, we can change that though
print(frame.sort_index(axis=1,ascending=False))

#to sort a series by its values, you make use of the sort_values method
obj=pd.Series([4,7,-3,2])
print(obj)

print(obj.sort_values())

#Any missing values are always sorted to the end

#when sorting,you can sort by some data

frame= pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
print(frame)

print(frame.sort_values(by='b'))

#to sort by multiple columns, we pass a list of names
print(frame.sort_values(by=['a','b']))


#Ranking
#ranking assigns ranks from one through the number of valid data points in an array
#The rank method for series and Dataframe are the place to look, ties are broken by assigning the mean rank

obj=pd.Series([7,-5,7,4,2,0,4])
print("\n")
print(obj)
print("\n")
print(obj.rank())

#Ranks can also be assigned acoording to the order in which they're observed in the data
print(obj.rank(method='first'))

#Ranks can also be assigned in descending order
print(obj.rank(ascending=False,method='max'))

#A dataframe can compute ranks over the columns and rows
frame=pd.DataFrame({'b':[4.3,7,-3,2],'a':[0,1,0,1],'c':[-2,5,8,-2.5]})
print(frame)
print("\n")
print(frame.rank(axis='columns'))