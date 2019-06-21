import tweepy
from textblob import TextBlob

consumer_key= '_______________________________'
consumer_secret= '_____________________________________'

access_token='____________________________________________________'
access_token_secret='_________________________________________________'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
