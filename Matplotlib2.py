import numpy as np
import pylab as pl

ds = np.random.normal(5.0,3.0,10000)
print(ds)
pl.hist(ds)
pl.xlabel('ds')
pl.show()
