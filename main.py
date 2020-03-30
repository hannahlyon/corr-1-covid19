#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 20:16:24 2020

@author: hannahlyon
"""

from responses import *
from predict import *

if __name__=='__main__':
    print(hello)
    # change the model in build_model parameter 
    # The options present are rf, nb, linear, ridge, knn 
    model, word2index, intent2index = build_model(model='rf')
    
    while True:
        question = input('Enter question or enter Q to exit: ')
        if question == 'Q':
            break
        predict_intent(question, model, word2index, intent2index)
        
    # how many cases are in my area -- sqllite db with kaggle data 