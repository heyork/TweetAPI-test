import requests
import tweepy
import json
import sys

#Authentication Keys
consumer_key = 	''
consumer_secret = ''
access_key = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

search_criteria = 'El Toro'

#Created tweet.txt file
tweets = open('tweets.txt', 'w')

results = api.search_users(q=search_criteria)

#Writes the names of the users being searched
for results in results:
	print (results.name)
	tweets.write(results.name)

tweets.close