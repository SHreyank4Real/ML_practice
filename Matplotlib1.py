import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
plt.plot(x,x,label='Linear')
plt.legend()
plt.show()

a = [100,21,31,41,53,63,65,26]
b = [14,52,14,61,161,16,61,62]
plt.scatter(a,b)
plt.show()
