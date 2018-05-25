import numpy as np
x = np.array([1,2,3,4,5,6,7])
x[0,] #returns 1st elements
x[:4] #returns 0 to 4th

np.save('x',x)
np.load("x.npy")
