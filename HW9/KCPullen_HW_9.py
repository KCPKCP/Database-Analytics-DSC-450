# -*- coding: utf-8 -*-
"""
Keiland Pullen

Winter 2022
DSC 450: Database Processing for Large-Scale Analytics
Assignment Module 9

"""

import json
import sqlite3
import urllib
import time

GeoTable = '''CREATE TABLE Geo(
    id varchar2(40),
    type varchar2(40),
    longitude varchar2(50),
    latitude varchar2(50),
    
    CONSTRAINT Geo_ID_PK 
        Primary Key (id)

); '''

UserTable = '''CREATE TABLE User(
    id varchar2(40),
    name varchar2(40),
    screen_name varchar2(40),
    description varchar2(100),
    friends_count number(10),
    
    Constraint ID_PK
        Primary Key(id)
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
    geo_id varchar2(40),
    
    CONSTRAINT Id_str_PK
        Primary Key(id_str),
    
    CONSTRAINT Tweet_FK 
        FOREIGN KEY (user_id)
        REFERENCES User(id),
        
    CONSTRAINT Geo_ID_FK
        FOREIGN KEY (geo_id)
        REFERENCES Geo(id)
    );'''

conn = sqlite3.connect("TwitterTwo.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS GEO")

cursor.execute(GeoTable)

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

f = open("Module9__errors.txt", "w", encoding="utf-8")

for i in range(lineCount):
    tweetLines = webFD.readline()
    try:
        tDict = json.loads(tweetLines.decode('utf8'))
        # print(tDict)
        #print(tDict['user']['id'])
        #print(tDict['geo'])
        # print("Hello")
        
        if tDict['geo'] != None:
            
            geo_id = tDict['user']['id']
            
            cursor.execute("INSERT OR IGNORE INTO Geo VALUES (?,?,?,?);",
                        (tDict['user']['id'], 
                         tDict['geo']['type'], 
                         tDict['geo']['coordinates'][0], 
                         tDict['geo']['coordinates'][1]) )
        else:
            geo_id = None
        
        #print(tDict['geo'])
        cursor.execute("INSERT OR IGNORE INTO User VALUES (?,?,?,?,?);", 
                       (tDict['user']['id'], tDict['user']['name'], tDict['user']['screen_name'], tDict['user']['description'],
                        tDict['user']['friends_count']))
        
        cursor.execute("INSERT OR IGNORE INTO Tweet VALUES (?,?,?,?,?,?,?,?,?,?,?);",
                        (tDict['created_at'], tDict['id_str'], tDict['text'], tDict['source'], tDict['in_reply_to_user_id'],
                         tDict['in_reply_to_screen_name'], tDict['in_reply_to_status_id'], tDict['retweet_count'],
                         tDict['contributors'], tDict['user']['id'], geo_id) )
        
        
    except ValueError:
        # print("Error on tweet - ",i)
        # print(tDict)
        errTweet = tDict
        
        f.write("Error on tweet number  " + repr(i))
        f.write("\n")
        f.write(str(errTweet) )
        f.write("\n")
          
        
f.close()

  

##################  Prob1.a.
start = time.time()

query1 = cursor.execute("SELECT * FROM Tweet where id_str LIKE '%88%' or id_str LIKE '%7777%' ")
print ("Total number of Tweets with 88 or 7777 anywhere is: ",len(query1.fetchall() ))
end = time.time()

print ("Start Time = ", start)
print ("End Time = ",end)
print ("The total time is ", ( end - start )," seconds")

print ("\n")




################   Prob1.b

print (' -------------------- ')
print('\n')

start = time.time()

print (lineCount)
print (tweetLines)
num = 1
for i in range(lineCount):
    tweetLines = webFD.readline()
    try:
        tDict = json.loads(tweetLines.decode('utf8'))

        if ('88' in tDict['id_str']) or ('7777' in tDict['id_str']):
            # print(num)
            num = num + 1

            
    except ValueError:
        print("Error here")

print('The number of 88 and 7777 was: ', num)

end = time.time()

print ("Start Time = ", start)
print ("End Time = ",end)
print ("The total time is ", ( end - start )," seconds")

print ('\n')


##################   Prob1.c

start = time.time()
qry2 = cursor.execute("SELECT COUNT(DISTINCT in_reply_to_user_id) From Tweet;")
qry2fetchall = cursor.fetchall()
print('The number of unique values is :',qry2fetchall)
      
end = time.time()
print ("Start Time = ", start)
print ("End Time = ",end)
print ("The total time is ", ( end - start )," seconds")


print ('\n')

#Prob1.d

replyUserIdSet = set() 

start = time.time()

for i in range(lineCount):
    tweetLines = webFD.readline()
    try:
        tDict = json.loads(tweetLines.decode('utf8'))

        replyUserIdSet.add(tDict['in_reply_to_user_id'])
            
    except ValueError:
        print("Nothing to see here")

#print(replyUserIdSet)
print ('The numnber of unique values is :', len(replyUserIdSet) ) 

end = time.time()
print ("Start Time = ", start)
print ("End Time = ",end)
print ("The total time is ", ( end - start )," seconds")



#####################  Prob1.e

print ('\n')
print ('\n')

import matplotlib.pyplot as plt
import numpy as np

txtLen = []
usrLen = []

for i in range(1, 41):
    tweetLines = webFD.readline()
    try:
        tDict = json.loads(tweetLines.decode('utf8'))

        textLength = len(tDict['text'])
        userLength = len(tDict['user']['screen_name'])
        
        txtLen.append(textLength)
        usrLen.append(userLength)
        
        # print(textLength, userLength)
            
    except ValueError:
        print("Nothing to see here")

x = np.array(txtLen)
y = np.array(usrLen)

plt.scatter(x, y)
plt.show()


conn.commit()
conn.close() 

