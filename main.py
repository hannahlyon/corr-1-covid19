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
    model, word2index = build_model()
    
    while True:
        question = input('Enter question or enter Q to exit: ')
        if question == 'Q':
            break
        intent = predict_intent(question, model, word2index)
        print(response_dict[intent])