#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:01:48 2020

@author: hannahlyon
"""

import tweepy
import numpy as np
import pandas as pd
from datetime import datetime
import json


# accounts for rate limiting and cursors
def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.TweepError:
            print('sleep zzz')
            time.sleep(16 * 60) 
        except StopIteration:
            return
        
        
if __name__=='__main__':
    with open('keys.txt', 'r') as file:
        keys = file.readlines()
    keys = [k.strip() for k in keys]
        
    api_key = keys[0]
    api_key_s = keys[1]
    access_token = keys[2]
    access_token_s = keys[3]
    
    auth = tweepy.OAuthHandler(api_key, api_key_s)
    auth.set_access_token(access_token, access_token_s)
    
    api = tweepy.API(auth)
    
    query = 'coronavirus'
    
    results = []
    tweets = tweepy.Cursor(api.search, q = query, result_type = 'recent', count = 100, tweet_mode = 'extended', lang = 'en')
    for t in limit_handler(tweets.items(5000)):
        results.append(t._json)
        
    with open('output_{}.txt'.format(datetime.today().strftime('%Y-%m-%d')), 'w') as outfile:
        json.dump(results, outfile) 