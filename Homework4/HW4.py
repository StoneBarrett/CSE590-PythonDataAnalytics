# Stone Barrett
# CSE 590: Python Data Analytics
# Homework 4

# Importing libraries
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LinearRegression, Ridge, Lasso
import mglearn

# Max_iter issue, explained in report
import warnings
warnings.filterwarnings("ignore")

# Problem 1
def Part1():
    # Loading dataset
    cancer = load_breast_cancer()
    x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=1)
    # Making model instances
    lsvm = LinearSVC()
    knn = KNeighborsClassifier()
    rf = RandomForestClassifier()
    # Cross val scores for each
    lsvmscores = cross_val_score(lsvm, cancer.data, y=cancer.target, cv=2)
    knnscores = cross_val_score(knn, cancer.data, cancer.target, cv=2)
    rfscores = cross_val_score(rf, cancer.data, cancer.target, cv=2)
    lsvmscores2 = cross_val_score(lsvm, cancer.data, cancer.target, cv=20)
    knnscores2 = cross_val_score(knn, cancer.data, cancer.target, cv=20)
    rfscores2 = cross_val_score(rf, cancer.data, cancer.target, cv=20)
    allscores = [lsvmscores, knnscores, rfscores, lsvmscores2, knnscores2, rfscores2]
    # Printing average of each cross val list
    for i in allscores:
        print("{:.2f}".format(i.mean()))
    # Most accurate is Random Forest with cv=20
    #print(x_train.shape, y_train.shape)
    rf.fit(x_train, y_train)
    predictedlabels = rf.predict(x_test)
    correctlabels = y_test
    confusion = confusion_matrix(correctlabels, predictedlabels)
    print(confusion)

# Problem 2
def Part2():
    # Making model instances
    lr = LinearRegression()
    ridge = Ridge()
    lasso = Lasso()
    # Loading datasets
    x, y = mglearn.datasets.load_extended_boston()
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
    # training
    lr.fit(x_train, y_train)
    ridge.fit(x_train, y_train)
    lasso.fit(x_train, y_train)
    # Printing scores
    # print("Training set score: {:.2f}".format(lr.score(x_train, y_train)))
    # print("Training set score: {:.2f}".format(ridge.score(x_train, y_train)))
    # print("Training set score: {:.2f}".format(lasso.score(x_train, y_train)))

    # Cross val scores r2 and mse
    lrscores = cross_val_score(lr, x_test, y_test, cv=10, scoring='r2')
    ridgescores = cross_val_score(ridge, x_test, y_test, cv=10, scoring='r2')
    lassoscores = cross_val_score(lasso, x_test, y_test, cv=10, scoring='r2')
    lrscores2 = cross_val_score(lr, x_test, y_test, cv=10, scoring='neg_mean_squared_error')
    ridgescores2 = cross_val_score(ridge, x_test, y_test, cv=10, scoring='neg_mean_squared_error')
    lassoscores2 = cross_val_score(lasso, x_test, y_test, cv=10, scoring='neg_mean_squared_error')
    allscores = [lrscores, ridgescores, lassoscores, lrscores2, ridgescores2, lassoscores2]
    # Printing
    for i in allscores:
        print("{:.2f}".format(i.mean()))


Part1()
Part2()