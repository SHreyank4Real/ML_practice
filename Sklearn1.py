#library focused on modeling data
from sklearn import datasets
from sklearn import metrics
from sklearn.svm import SVC  #support vector classifier and support vector machine

ds = datasets.load_iris() #loading iris from dataset

model = SVC()
model.fit(ds.data,ds.target)
expected = ds.target
predected = model.predict(ds.data)
print(metrics.classification_report(expected,predected))
