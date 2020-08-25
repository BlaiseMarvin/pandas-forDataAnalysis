#This section takes you through the fundamental mechanics of interacting with the data contained in a series and dataframe
#Reindexing
#reindex means create a new object with data conformed to a new index

import pandas as pd 
import numpy as np 

obj=pd.Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
print(obj)

#callin reindex, rearranges the data to the new index, introducing missing values, if any values were previously not present

obj2=obj.reindex(['a','b','c','d','e'])
print(obj2)


#when reindexing, you may need to interpolate, the missing values, this can basically be through adding ffill to the method

obj3=pd.Series(['blue','purple','yellow'],index=[0,2,4])
print(obj3)

obj4=obj3.reindex(range(6),method='ffill')
print(obj4)

#reindexing can alter either the (row) index,columns or both. when passed only a sequence, it reindexes the rows in the result

frame= pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns=['Ohio','Texas','California'])
print(frame)


frame2=frame.reindex(['a','b','c','d'])
print(frame2)

#Columns can be reindexed with the columns keyword
states=['Texas','Utah','California']

frame3=frame.reindex(columns=states)
print(frame3)

