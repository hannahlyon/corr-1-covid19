#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 20:16:15 2020

@author: hannahlyon
"""
import pandas as pd
import numpy as np
from nltk.stem import WordNetLemmatizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import RidgeClassifier

from responses import *

wnl = WordNetLemmatizer()

def build_model(model='linear'):
    df = pd.read_csv('covid19_questions2.csv')
    df = df.sample(len(df))


    corpus = [wnl.lemmatize(word.lower()) for sent in df['sentence'].values 
              for word in sent.split(' ')]
    
    intent2index = {v:i for i,v in enumerate(df['intent'].unique())}
    word2index = {v:i for i,v in enumerate(set(corpus))}
    
    X = []
    for i,row in df.iterrows():
        temp = np.zeros(len(word2index))
        for word in row['sentence'].split(' '):
            new_word = wnl.lemmatize(word)
            if new_word in word2index:
                idx = word2index[new_word]
                temp[idx] = 1
        X.append(temp)
    X = np.array(X)
    y = df['intent'].map(intent2index).values
    # adding option for different models 
    if model == 'rf':
        lr = RandomForestClassifier(n_estimators = 100).fit(X,y)
        model_type = 'rf'
    if model == 'nb':
        lr = BernoulliNB().fit(X,y)
        model_type = 'nb'
    if model =='linear':
        lr = LogisticRegression(multi_class='multinomial').fit(X,y)
        model_type = 'linear'
    if model == 'knn':
        lr = KNeighborsClassifier(n_neighbors=3).fit(X, y)
        model_type = 'knn'
    if model == 'ridge':
        lr = RidgeClassifier().fit(X, y)
        model_type = 'ridge'


    return lr, word2index, intent2index
    
    
def predict_intent(question, model, word2index, intent2index):
    index2intent = {v:k for k,v in intent2index.items()}
    
    question = question.replace('?','')
    question = question.lower().split(' ')
    
    one_hot = np.zeros(len(word2index))
    for word in question:
        new_word = wnl.lemmatize(word)
        if new_word in word2index:
            idx = word2index[new_word]
            one_hot[idx] = 1
    one_hot = one_hot.reshape(1, -1)
    
    pred = model.predict(one_hot)
    return response_dict[index2intent[pred[0]]]
\

