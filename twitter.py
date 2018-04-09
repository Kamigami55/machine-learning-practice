# Code from Siraj Raval's Youtube Video
# Twitter Sentiment Analysis - Learn Python for Data Science #2
# https://youtu.be/o_OZdbCzHUA

import tweepy
from textblob import TextBlob

# Import consumer_key, consumer_secret, access_token, access_token_secret from twitterKey.py
from twitterKey import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
