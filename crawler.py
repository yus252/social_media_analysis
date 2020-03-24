import tweepy
import csv
import pandas as pd
import datetime
####input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####Coronavirus

start_date = datetime.datetime(2020, 2, 23, 00, 00, 00)
end_date = datetime.datetime(2020, 2, 29, 00, 00, 00)

# Open/Create a file to append data
csvFile = open('week4.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#Coronavirusi china",count=100,
                           lang="en",
                           since=start_date,
                           until=end_date).items():
    #print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
