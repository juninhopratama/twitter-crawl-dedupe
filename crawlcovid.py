# -*- coding: utf-8 -*-

#requierements
import tweepy
import re
import pandas as pd
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#script goes here
data=[]
search_results = api.search(q='covid @kemenkesRI OR @satgascovid19id -filter:retweets',lang='id', count=500)

for mention in search_results:
    tweet =mention.text
    tanggal= mention.created_at
    retweet=mention.retweet_count
    username=mention.author.screen_name
    userID = mention.author.id
    usernameReal = mention.author.name
    userLoc = mention.author.location
    userDesc = mention.author.description
    data.append([tweet,tanggal,retweet,username,userID,usernameReal,userLoc,userDesc])

datatw = pd.DataFrame(data)
datatw.index.name = 'Index'
datatw.to_csv("result.csv",header=["Tweet","Tanggal","Jumlah Retweet","Username","User ID","Name","Location","User Desc"])