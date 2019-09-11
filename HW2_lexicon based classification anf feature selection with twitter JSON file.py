""" hwcode.py
    Write the code for the HW exercises in this file.
"""
# Anthony: HW2 Grade - 38/30

import csv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score
 


def classify_tweets_lexicon(csv_filename, positive_lexicon, negative_lexicon):
    '''
    Classifies each tweet in the test split of csv_filename as
    either having positive or negative sentiment.

    :param str csv_filename: The file path of the twitter dataset
    :param list positive_lexicon: A list of words that represent
                                  positive sentiment
    :param list negative_lexicon: A list of words that represent
                                  negative sentiment
    :return: A float (macro F1 score on test split)
    '''
    # Write code for exercise 1 part 1 here
    predictions=[]
    X=[]
    infile=open(csv_filename, encoding="cp1252")
    myCsv=csv.reader(infile,delimiter=',')
    for row in myCsv:
        pos=0
        neg=0
        tweet=row[-1].lower()
        
        for word in tweet.split():
            if word in positive_lexicon:
                pos += 1
            elif word in negative_lexicon:
                neg += 1
        if pos >= neg:
            predictions.append("positive")
        elif neg > pos:
            predictions.append("negative")
        
        X.append(row[0])
    X=np.array(X)
    y=np.array(predictions)
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    f1_test = float(f1_score(y_test,X_test,average='macro'))
    return f1_test

def classify_tweets(csv_filename):
    '''
    Train a classifier and to predict sentiment on tweets.

    :param str csv_filename: The file path of the twitter dataset
    :return: A float (macro F1 score on test split)
    '''
    # Write code for exercise 1 part 2 here
    y=[]
    X_txt=[]
    infile=open(csv_filename, encoding="cp1252")
    myCsv=csv.reader(infile,delimiter=',')
    for row in myCsv:
        X_txt.append(row[-1])
        y.append(row[0])
    X_txt = np.array(X_txt)
    y = np.array(y)
    
    X_txt_train, X_txt_test, y_train, y_test = train_test_split(X_txt,y,test_size=0.2,random_state=42)
    
    vec = CountVectorizer(ngram_range=(1,1), min_df = 1)
    vec.fit(X_txt_train)
    X_train=vec.transform(X_txt_train)
    X_test=vec.transform(X_txt_test)
    
    params = {"C":[0.01]}
    svc=LinearSVC()
    clf=GridSearchCV(svc,params,scoring='f1_macro',cv=2)
    
    clf.fit(X_train, y_train)
    
    f1_test=float(f1_score(y_test,clf.predict(X_test),average='macro'))
    return f1_test

def hospital_p1(csv_filename):
    '''
    Train a classifier on colon cancer gene expression data.

    :param str csv_filename: The file path of the colon dataset
    :return: A float (Best GridSearchCV macro F1)
    '''
    # Write code for exercise 1 part 2 here
    y=[]
    X=[]
    X1=[]
    header=True
    infile=open(csv_filename, encoding="cp1252")
    myCsv=csv.reader(infile,delimiter=',')
    for row in myCsv:
        if header:
            header=False
        else:
            X1.append([int(x) for x in row[1:]])
            y.append(int(row[0]))       
    for i in X1:
        for ind, item in enumerate(i):
            if i[ind] == -2:
                i[ind]=0
    
    X = np.array(X1)
    y = np.array(y)
    #X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    pipe = Pipeline([ ('skb', SelectKBest(chi2)), ("clf", SVC())])
    params = {"clf__C":[0.001,0.01,0.1, 1., 10.],
              "skb__k":[100, 500, 'all'],
              "clf__kernel":['linear','rbf']} 
    clf = GridSearchCV(pipe, params, scoring='f1_macro', cv=5)
    clf.fit(X,y)

    return float(clf.best_score_)

def hospital_p2(csv_filename):
    '''
    Train a classifier on colon cancer gene expression data.

    :param str csv_filename: The file path of the colon dataset
    :return: A list of the top 5 chi2
             feature names (strings) ["feature_1", ..., "feature_72"]
    '''
    # Write code for exercise 1 part 2 here
    y=[]
    X=[]
    X1=[]
    feat=[]
    out=[]
    header=True
    infile=open(csv_filename, encoding="cp1252")
    myCsv=csv.reader(infile,delimiter=',')
    for row in myCsv:
        if header:
            header=False
            feat.append(row[1:])
        else:
            X1.append([int(x) for x in row[1:]])
            y.append(row[0])       
    for i in X1:
        for ind, item in enumerate(i):
            if i[ind] == -2:
                i[ind]=0
    
    X = np.array(X1)
    y = np.array(y)
    #X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    pipe = Pipeline([ ('skb', SelectKBest(chi2)), ("clf", SVC())])
    params = {"clf__C":[0.001,0.01,0.1, 1., 10.],
              "skb__k":[5,10,100,500, 'all'],
              "clf__kernel":['linear','rbf']} 
    clf = GridSearchCV(pipe, params, scoring='f1_macro', cv=3) 
    clf.fit(X,y)
    # Anthony: This works, but you don't need GridSearchCV for this question
    # You can simply use SelectKBest. I'm not sure if we get the best features
    # for the entire dataset, or simply for one fold.
    ind1=clf.best_estimator_.named_steps['skb'].get_support(indices=True)
    for i in ind1[0:5]:
        # Anthony: You should not need "-1" here. (-2 points)
        out.append(feat[0][i-1])
    return out



def better_model(csv_filename):
    '''
    Train a classifier and to predict sentiment on tweets.

    :param str csv_filename: The file path of the twitter dataset
    :return: A float (macro F1 score on test split)
    '''
    # Write code for exercise 1 part 2 here
    y=[]
    X_txt=[]
    infile=open(csv_filename, encoding="cp1252")
    myCsv=csv.reader(infile,delimiter=',')
    for row in myCsv:
        X_txt.append(row[-1])
        y.append(row[0])
    X_txt = np.array(X_txt)
    y = np.array(y)
    
    X_txt_train, X_txt_test, y_train, y_test = train_test_split(X_txt,y,test_size=0.2,random_state=42)
    vec = CountVectorizer(ngram_range=(1,2), 
                          min_df = 5,max_df=0.50,max_features=10000)
    vec.fit(X_txt_train)
    X_train=vec.transform(X_txt_train)
    X_test=vec.transform(X_txt_test)
    params = {"C":[0.01]}
    svc=LinearSVC()
    clf=GridSearchCV(svc,params,scoring='f1_macro',cv=2)
    
    clf.fit(X_train, y_train)
    
    f1_test=float(f1_score(y_test,clf.predict(X_test),average='macro'))
    
    
    return f1_test

def competition(csv_train_filename, csv_test_filename):
    '''
    Train a classifier and to predict sentiment on tweets.

    :param str csv_train_filename: The train data file path of the twitter dataset
    :param str csv_test_filename: The test data  file path of the twitter dataset
    :return: A np.ndarray The output of clf.predict()
    '''
    # Write code for exercise 1 part 2 here
    y=[]
    X_txt=[]
    X_txtt=[]
    yt=[]
    trainfile=open(csv_train_filename, encoding="cp1252")
    testfile=open(csv_test_filename, encoding="cp1252")
    myCsvtr=csv.reader(trainfile,delimiter=',')
    for row in myCsvtr:
        X_txt.append(row[-1])
        y.append(row[0])
    X_txt = np.array(X_txt)
    y = np.array(y)
    
    myCsvt=csv.reader(testfile,delimiter=',')
    for row in myCsvt:
        X_txtt.append(row[-1])
        yt.append(row[0])
    X_txtt = np.array(X_txtt)
    yt = np.array(yt)
    
    vec = CountVectorizer(ngram_range=(1,2), 
                          min_df = 5,max_df=0.50,max_features=10000)
    vec.fit(X_txt)
    X_train=vec.transform(X_txt)
    X_test=vec.transform(X_txtt)
    params = {"C":[0.01]}
    svc=LinearSVC()
    clf=GridSearchCV(svc,params,scoring='f1_macro',cv=2)
    
    clf.fit(X_train,y)
    
    out_nparray=np.array(clf.predict(X_test))
    
    
    return out_nparray

