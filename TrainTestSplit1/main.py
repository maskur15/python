from sklearn import datasets
from sklearn.model_selection import train_test_split
import  numpy as np
iris = datasets.load_iris()
#split it in features and label
x = iris.data
y = iris.target
print(x.shape)
print(y.shape)
#hours of study vs good / bad grades
#10 different students
#train with 8 students
#predict with the remaining 2
#level of accuracy
X_train, X_test, y_train, y_test= train_test_split(x,y,test_size=0.2)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)