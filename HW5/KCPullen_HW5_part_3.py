# -*- coding: utf-8 -*-
"""
Keiland Pullen

Winter 2022
DSC 450: Database Processing for Large-Scale Analytics
Assignment Module 5
"""


import json
import sqlite3
import urllib


TwitterTable = '''CREATE TABLE Tweet(
    created_at varchar2(40),
    id_str varchar2(40),
    text varchar2(250),
    source varchar2(100),
    in_reply_to_user_id number(25),
    in_reply_to_screen_name varchar(40),
    in_reply_to_status_id number(25),
    retweet_count number(10),
    contributors varchar2(100)
    );'''

conn = sqlite3.connect("Twitter.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS TWEET")

cursor.execute(TwitterTable)

tweetData = 'http://cdmgcsarprd01.dpu.depaul.edu/DSC450/tweet_data.txt'

webFD = urllib.request.urlopen('http://cdmgcsarprd01.dpu.depaul.edu/DSC450/tweet_data.txt')

webFD.readline()

ln = webFD.readline()

tweeter = json.loads(ln[6:])

tweeter.keys()

# print (ln[6:]) 

# print(tweeter)
# print("\n")
# print(tweeter.keys())

# print(tweeter['created_at'])
# print(tweeter['id_str'])
# print(tweeter['text'])
# print(tweeter['source'])
# print(tweeter['in_reply_to_user_id'])
# print(tweeter['in_reply_to_screen_name'])
# print(tweeter['in_reply_to_status_id'])
# print(tweeter['retweet_count'])
# print(tweeter['contributors'])

# print("\n")

cursor.execute("INSERT OR IGNORE INTO Tweet VALUES (?,?,?,?,?,?,?,?,?);", 
                   (tweeter['created_at'], tweeter['id_str'], tweeter['text'], tweeter['source'], tweeter['in_reply_to_user_id'], 
                    tweeter['in_reply_to_screen_name'], tweeter['in_reply_to_status_id'], tweeter['retweet_count'], 
                    tweeter['contributors']))


DisplayTweet = cursor.execute("SELECT * FROM TWEET;").fetchall()
for Rows in DisplayTweet:
    print(Rows)



