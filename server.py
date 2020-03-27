import sys
import math
from flask import Flask, render_template, request

from colour import Color
from responses import *
from predict import *

app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('home.html')  #,record=dict_tweets, median=median_score) #CHECK:the url in the html!!!, color


# @app.route("/<name>")
# def tweets(name):
#     "Display the tweets for a screen name color-coded by sentiment score"
#     dict_tweets=fetch_tweets(api,name)
#     add_color(dict_tweets['tweets'])
#
#     list_tweets=dict_tweets['tweets']
#
#     median_score=round(median([tweet['score'] for tweet in list_tweets]),4)
#
#     return render_template('tweets.html',record=dict_tweets, median=median_score) #CHECK:the url in the html!!!, color

@app.route("/get")
def get_bot_response():
    question = request.args.get('msg')
    prediction = predict_intent(question, model, word2index, intent2index)
    return str(prediction)



model, word2index, intent2index = build_model()



#gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log server:app twitter.csv

# i = sys.argv.index('server:app')
# twitter_auth_filename = sys.argv[i+1]
#twitter_auth_filename = 'twitter.csv'
#api = authenticate(twitter_auth_filename)

app.run(host='0.0.0.0', port=5000)
