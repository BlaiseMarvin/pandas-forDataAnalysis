#pandas index objects are responsible for holding axis labels and other meta data
import pandas as pd 
obj = pd.Series(range(3),index=['a','b','c'])
print(obj)

index=obj.index
print(index)

#Index objects are immutable and cannot be modified by the user

#frame 3

data={
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
    'year':[2000,2001,2002,2001,2002,2003],
    'pop':[1.5,1.7,3.6,2.4,2.9,3.2]
}
zi=pd.Index([2000,2001,2002,2003,2004,2005])
frame3=pd.DataFrame(data,index=zi)
print(frame3)
print(frame3.columns)
print('Ohio' in frame3.columns)

#A pandas index can contain duplicate labels

#Selection with duplicate labels, will select all occurences of that label

