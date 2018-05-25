import pandas as pd
ufo = pd.read_table('http://bit.ly/uforeports',sep=",")
#print(ufo.head(5))
#print(ufo['State'])
ufo['Location'] = ufo.City +" "+ufo.State
#print(ufo.head(5))
print(ufo.shape)
print(ufo.columns)
print(ufo.dtypes)
