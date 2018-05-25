import pandas as pd
ufo = pd.read_table('http://bit.ly/uforeports',sep=",")
ufo.drop('Colors Reported',axis=1,inplace=True)
print(ufo.head(5))
ufo.drop(['State','Time'],axis=1,inplace=True)
print(ufo.head(5))
#sorting
print(ufo.City.sort_values(ascending=False).head(5))
