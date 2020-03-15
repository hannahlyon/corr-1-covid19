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

wnl = WordNetLemmatizer()

def build_model():
    df = pd.read_csv('covid19_questions.csv')
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
    
    lr = LogisticRegression(multi_class='multinomial').fit(X,y)
    return lr, word2index
    
    
def predict_intent(question, model, word2index):
    index2intent = {v:k for k,v in word2index.items()}
    
    question = question.lower().split(' ')
    # remove punctuation
    one_hot = np.zeros(len(word2index))
    for word in question:
        new_word = wnl.lemmatize(word)
        if new_word in word2index:
            idx = word2index[new_word]
            one_hot[idx] = 1
    one_hot = one_hot.reshape(1, -1)
    pred = model.predict(one_hot)
    pred = index2intent[pred[0]]
    return pred