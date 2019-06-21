import re
import time,datetime
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier

def gradiente(p):
    name = 'SGDClassifier'
    dataset = pd.read_csv(p)
    X = dataset.values[:, 2:]
    Y = dataset.values[:, 1].astype(int)
    
    cv = 2
    clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
    scores = cross_val_score(clf, X, Y, cv=cv)
    print(scores)
    return name,scores
    
def gauss(p):
    name = 'GaussianNB'
    dataset = pd.read_csv(p)
    X = dataset.values[:, 2:]
    Y = dataset.values[:, 1].astype(int)
    
    cv = 2
    clf = GaussianNB()
    scores = cross_val_score(clf, X, Y, cv=cv)
    print(scores)
    return name,scores
    
def knn(p):
    name = 'KNeighborsClassifier'
    dataset = pd.read_csv(p)
    X = dataset.values[:, 2:]
    Y = dataset.values[:, 1].astype(int)
    
    cv = 2
    clf = KNeighborsClassifier(n_neighbors=2)
    scores = cross_val_score(clf, X, Y, cv=cv)
    print(scores)
    return name,scores
    
def neurona(p):
    name = 'MLPClassifier'
    # numero de lineas
    dataset = pd.read_csv(p)
    X = dataset.values[:, 2:]
    Y = dataset.values[:, 1].astype(int)
    
    cv = 2
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
        hidden_layer_sizes=(5, 2), random_state=1)
    scores = cross_val_score(clf, X, Y, cv=cv)
    print(scores)
    return name,scores
    
def training(p):
    name = 'SVC'
    dataset = pd.read_csv(p)
    X = dataset.values[:, 2:]
    Y = dataset.values[:, 1].astype(int)
    
    cv = 2
    clf = svm.SVC(kernel='linear', C=1)
    scores = cross_val_score(clf, X, Y, cv=cv)
    print(scores)
    return name,scores

def tp(f,p):
    t1 = time.time()
    r1,r2=f(p)
    t2 = time.time()
    t3 = t2 -t1
    print(t1,t2)
    print(t3)
    return r1,r2,t1,t2,t3

p_ls = ["data/01/train100.csv","data/01/train1k.csv",
    "data/01/train2k.csv","data/01/train3k.csv",
    "data/01/train4k.csv"]
f_ls = [gradiente,gauss,neurona,training,knn]
data = []
for x in p_ls:
    print('>>1')
    print(x)
    for x1 in f_ls:
        print('>>2')
        for x2 in range(1):
            r1,r2,r3,r4,r5=tp(x1,x)
            d1=re.findall(r"/(.+)/",x)[0]
            d2=re.findall(r"/train(.+)\.",x)[0]
            d={'data':d1,'tamano':d2,'nombre':r1,'score':r2,
                't1':r3,'t2':r4,'t3':r5}
            data.append(d)
            print(data)
print('>>>>>> fin')
print(data)
