#Numpy's ufunc methods also work with pandas
import numpy as np 
import pandas as pd 

frame=pd.DataFrame(np.random.randn(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
print(frame)

#applying the absolute method
print(np.abs(frame))

#another frequent operation is applying a function on one dimensional arrays to each column or row
#DataFrame's apply method does this exactly

f=lambda x:x.max()-x.min()
print(frame)
print(frame.apply(f,axis=1))

#mtds
def fi(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])

print(frame.apply(fi,axis=0))

