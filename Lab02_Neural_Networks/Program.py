import sklearn
import pandas
import numpy as np


data=pandas.read_csv("iris.data", header=None)
print(data)
#You can add an argument, header, and set it equal to none so the command doesn't read the first line as a header



import matplotlib.pyplot as plt
import seaborn as sns
sns.pairplot( data=data,vars=(0,1,2,3), hue=4 )
plt.show()
#Yes, you can. The Iris-setosa can be easily identified. The Iris-versicolor and the Iris-virginica are hard to tell apart because their points are mixed together
#on the majority of the graphs.

data=np.array(data)


X=data[:,0:4]
y=data[:,4]
print(X.shape)
print(y.shape)

from sklearn.utils import shuffle
X,y=shuffle(X,y,random_state=1)

print(X)
print("\n\n", y)
#I verified that they were shuffled and that they were shuffled identically by printing both arrays. 
#random_state is the seed used by the random number generator.
#It can be very useful because you can set it equal to a number which allows anyone to reproduce the same results as your neural network.


trainX=X[:110]
trainy=y[:110]
testX=X[110:]
testy=y[110:]


from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=[3,2], random_state=1, max_iter = 2000)
clf.fit(trainX, trainy)



print(clf.coefs_)



prediction=clf.predict(testX)

print(prediction)
print("\n\n", testy)


print(clf.score(trainX,trainy))
print(clf.score(testX,testy))



from sklearn.model_selection import cross_validate
cv_results = cross_validate(clf, X, y, cv=4)
print(cv_results)

