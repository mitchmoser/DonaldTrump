#!/usr/bin/env python3
import markovify
import tweepy
import string
import html
import json
import re
# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# @realDonaldTrump's twitter ID is 25073877
twitterID = '25073877'

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # load json object from tweet
        dump = json.dumps(status._json)
        jsonStr = json.loads(dump)
        # get numeric ID of tweet for reply
        reply = jsonStr['id']
        if jsonStr['user']['id'] == int(twitterID):
            # get the account's @username
            handle = "@" + jsonStr['user']['screen_name'] + " "
            # get most recent tweets from profile (200 is max allowed)
            timeline = api.user_timeline(screen_name = 'realDonaldTrump', count = 200, tweet_mode="extended", include_rts = False)

            mark = ""

            for data in timeline:
                # load json object from tweet
                bulk = json.dumps(data._json)
                load = json.loads(bulk)
                tweet = html.unescape(load['full_text'])
                # remove hyperlinks from tweets
                tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet.strip())
                # ensure tweets end in punctuation
                if tweet[-1] not in string.punctuation:
                    tweet = tweet + "."
                mark += tweet + " "

            text_model = markovify.Text(mark)
            tweet = text_model.make_sentence()
            api.update_status(handle + tweet, in_reply_to_status_id = reply)

    def on_error(self, status_code):
        print('Error: ' + repr(status_code))
        return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=[twitterID]) # filter stream on user's unique numeric ID
