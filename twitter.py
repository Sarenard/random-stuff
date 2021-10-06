#By Loris_redstone#2290 on discord

from tweepy.streaming import StreamListener
from datetime import datetime
from tweepy import Stream
import threading
import random
import tweepy
import json
import time
import os

global nb
nb = 0
def auth():
    consumer_key = "SECRET"
    consumer_secret = "SECRET"
    access_token = "SECRET"
    access_token_secret = "SECRET"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api,auth
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')
class listener(StreamListener):
    def on_data(self, data):
        global texts, nb
        all_data = json.loads(data)
        id_tweet = all_data['id_str']
        tweet = all_data['text']
        username = all_data['user']['screen_name']
        if not contains_word(tweet, 'RT') and not contains_word(tweet, 'exemple'):
            nb += 1
            api.update_status(
                status='@' + username + ' ' + tweet.replace("taken place", "taken deez nuts").replace("team", "deez nuts").replace("us", "deez nuts").replace("you", "deez nuts").replace("the community", "deez nuts"),
                in_reply_to_status_id=id_tweet
            )
        return True
    def on_error(self, status):
        print(status)
api, auth = auth()
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["taken place", "team", "teams", "us", "you", "the community"])
