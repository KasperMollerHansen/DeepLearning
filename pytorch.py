#%%
import torch
import numpy as np
#%%
d1 = np.random.rand(2, 3)
print('np array:\n', d1)
t1 = torch.tensor(d1)
print('torch tensor:\n', t1)
d2 = t1.numpy()
print('back to np:\n', d2)
# %%
tensorOfZeros = torch.zeros([2,4],dtype=torch.int32)
print("tensorOfZeros:\n",tensorOfZeros)
tensorOfnumbers = torch.tensor([1,2,10],dtype=torch.int32)
print("tensorOfnumbers:\n",tensorOfnumbers)
npArray = np.random.rand(2,3)
tensorFromNumPy = torch.tensor(npArray)
print("tensorFromNumPy:\n",tensorFromNumPy)
newShape = tensorFromNumPy.reshape((3,2))
print("newShape:\n",newShape)
print("newShape.sum(dim=0):\n",newShape.sum(dim=0))
print("newShape.float():\n",newShape.float())
#%%
w=torch.tensor(2.0,requires_grad=True)
x=torch.rand((2,2))
x2=x*w
L=torch.sum(x2,axis=(0,1))
print("w.grad:\n",w.grad)
L.retain_grad()
x2.retain_grad()
L.backward(retain_graph=True)
print("w.grad:\n",w.grad)
# %%
