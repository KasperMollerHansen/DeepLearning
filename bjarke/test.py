#%%
import numpy as np
import matplotlib.pyplot as plt
hej = 4
print(hej)
print(np.exp(2))
x = np.linspace(0,10,100)
plt.plot(x, [hej for _ in range(len(x))])
plt.show()
#%%