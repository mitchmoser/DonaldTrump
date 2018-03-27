# Donald J Trump
This bot that interacts with Twitter's Streaming API and automatically replies to a user's posts.

## Check It Out [Here](https://twitter.com/reelDonnyDrumpf/with_replies)

### How It Works

In order to view tweets in real-time, use [Tweepy](http://docs.tweepy.org/en/v3.6.0/index.html) as a wrapper for [Twitter's Streaming API](http://docs.tweepy.org/en/v3.6.0/streaming_how_to.html)

Twitter assigns a unique numerical ID to every user and every tweet.

The stream object's filter can be set to a user's ID; this will only display tweets by or tagging that user's account.

To filter content to only tweets *by the user*, incoming user IDs are parsed and compared to the desired user ID.

Once this is done, the user's latest 200 tweets are scraped from their timeline and packed into a string variable.

These tweets are fed into [markovify](https://github.com/jsvine/markovify) in order to generate a new tweet.

The tweet is then sent as a reply to the user's most recent post.
