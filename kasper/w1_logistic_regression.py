#%%
import numpy as np
import sklearn.model_selection
import matplotlib.pyplot as plt
from mlxtend.data import mnist_data
#%%
#load data
X, y = mnist_data()
#we just focus on 1's and 0's:
keep=(y==0) | (y==1)
X=X[keep,:]
y=y[keep]
y=np.expand_dims(y,1)
#%%
# create a loss function:
def avrLoss(y,a):

  #INSERT CODE

  return np.mean(loss)
#%%
#test loss function:
#(just run this cell and see what happens)
loss=avrLoss(np.array([0,1,0,1]),np.linspace(.1,.9,4))
assert np.all(loss==0.5543313122608056)