#consider a small series with duplicate indices
import pandas as pd 
import numpy as np 

obj=pd.Series(range(5),index=['a','a','b','b','c'])
print(obj)

#tell whether the indexing label is unique or not
print(obj.index.is_unique)

