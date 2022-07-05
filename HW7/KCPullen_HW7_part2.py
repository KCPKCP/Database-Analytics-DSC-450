# -*- coding: utf-8 -*-
"""
Keiland Pullen

Winter 2022
DSC 450: Database Processing for Large-Scale Analytics
Assignment Module 7

Part 2
"""

import json
import sqlite3
import urllib


UserTable = '''CREATE TABLE User(
    id varchar2(40),
    name varchar2(40),
    screen_name varchar2(40),
    description varchar2(100),
    friends_count number(10)
    );'''


TwitterTable = '''CREATE TABLE Tweet(
    created_at varchar2(40),
    id_str varchar2(40),
    text varchar2(250),
    source varchar2(100),
    in_reply_to_user_id number(25),
    in_reply_to_screen_name varchar(40),
    in_reply_to_status_id number(25),
    retweet_count number(10),
    contributors varchar2(100),
    user_id varchar2(40),
    
    CONSTRAINT Tweet_FK 
        FOREIGN KEY (user_id)
        REFERENCES User(id)
    );'''

conn = sqlite3.connect("TwitterTwo.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS USER")

cursor.execute(UserTable)

cursor.execute("DROP TABLE IF EXISTS TWEET")

cursor.execute(TwitterTable)


webFD = urllib.request.urlopen('http://dbgroup.cdm.depaul.edu/DSC450/Module7.txt')

tweetLines = webFD.readline()

lineCount = 0
for line in tweetLines:
    lineCount = lineCount + 1
print(lineCount)

f = open("Module7_errors.txt", "w", encoding="utf-8")

for i in range(lineCount):
    tweetLines = webFD.readline()
    try:
        tDict = json.loads(tweetLines.decode('utf8'))
        #print(tDict)
        # print("Hello")
        cursor.execute("INSERT OR IGNORE INTO User VALUES (?,?,?,?,?);", 
                       (tDict['user']['id'], tDict['user']['name'], tDict['user']['screen_name'], tDict['user']['description'],
                        tDict['user']['friends_count']))
        
        cursor.execute("INSERT OR IGNORE INTO Tweet VALUES (?,?,?,?,?,?,?,?,?,?);",
                        (tDict['created_at'], tDict['id_str'], tDict['text'], tDict['source'], tDict['in_reply_to_user_id'],
                         tDict['in_reply_to_screen_name'], tDict['in_reply_to_status_id'], tDict['retweet_count'],
                         tDict['contributors'], tDict['user']['id']) )
                    
        
    except ValueError:
        # print("Error on tweet - ",i)
        # print(tDict)
        errTweet = tDict
        
        f.write("Error on tweet number  " + repr(i))
        f.write("\n")
        f.write(str(errTweet) )
        f.write("\n")
          
        
f.close()

# result = cursor.execute ("SELECT * FROM User")
# result.fetchall()

conn.commit()
conn.close() 
