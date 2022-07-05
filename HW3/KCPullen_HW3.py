# -*- coding: utf-8 -*-
"""
Keiland Pullen

Winter 2022
DSC 450: Database Processing for Large-Scale Analytics
Assignment Module 3
"""

import sqlite3

conn = sqlite3.connect('dsc450_hw3.db')

droptbl = """
    DROP TABLE Animal;
    """
    
createtbl = """
CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR2(30) NOT NULL,
  ACategory VARCHAR2(18),
  TimeToFeed NUMBER(4,2),

  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);
"""

inserts = ["INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);", 
           "INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);", 
           "INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);", 
           "INSERT INTO Animal VALUES(4, 'Grizzly bear', 'common', 3.0);", 
           "INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.5);", 
           "INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.75);", 
           "INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.25);", 
           "INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.75);", 
           "INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.5);", 
           "INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.25);", 
           "INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.5);"]

cursor = conn.cursor()



cursor.execute(createtbl)   # create the Animal table
for ins in inserts:         # insert the rows
    cursor.execute(ins)
    print(ins)
    
    
import os
os.getcwd()

result = cursor.execute('SELECT * FROM Animal')
result.fetchall()

'''cursor.execute(droptbl);'''

''' 
    1. Find all the animals that take less than 2.5 hours to feed
'''
timeToFeed = cursor.execute('SELECT * FROM Animal WHERE TimeToFeed < 2.5')
timeToFeed.fetchall()

'''
    2. Find both the rare and exotic animals in a single query.
'''
rareAndExotic = cursor.execute('SELECT * FROM Animal WHERE ACategory="rare" or ACategory="exotic" ')
rareAndExotic.fetchall()

'''
    3. Return the listings for all animals whose rarity is missing (NULL) in the database.
'''
rarityMissing = cursor.execute('SELECT * FROM Animal WHERE ACategory is NULL')
rarityMissing.fetchall()

'''
    4. Find the rarity rating of all animals that require between 1 and 2.5 hours to be fed.
    
'''

rarityRatingFeed = cursor.execute('SELECT ACategory FROM Animal WHERE TimeToFeed >= 1 and TimeTOFeed <= 2.5')
rarityRatingFeed.fetchall()

'''
    5. Find the min and max feeding time amongst all the animals in the zoo.
'''
minMaxFeedingTime = cursor.execute('SELECT MIN(TimeToFeed), MAX(TimeToFeed) from Animal')
minMaxFeedingTime.fetchall()

'''
    6. Find the average feeding time for all of the exotic animals.
'''
avgFeedingTime = cursor.execute('SELECT AVG(TimeToFeed) from Animal')
avgFeedingTime.fetchall()

'''
    7. Determine how many NULLs there are in the ACategory column using SQL
'''
howManyNulls = cursor.execute('SELECT COUNT(*) - COUNT(ACategory) FROM Animal' )
howManyNulls.fetchall()

'''
    8. Find all animals named 'Alpaca', 'Llama' or any other animals that are not listed as exotic
'''
allAlpachaLlama = cursor.execute('SELECT * FROM Animal where AName="Alpaca" or AName="Llama" or ACategory != "exotic" ')
allAlpachaLlama.fetchall()


result = cursor.execute('SELECT * FROM Animal')
#result.fetchall()
allAnimalsFile = result.fetchall()

print(allAnimalsFile)
af = open("animal.txt","w")

separator = ", "
for animalTxt in allAnimalsFile:
    af = open("animal.txt","a")
    print(separator.join(map(str, animalTxt)) )
    af.write(separator.join(map(str, animalTxt)) )
    af.write("\n")

af.close()

conn.commit()
conn.close()

import os

os.getcwd()
os.chdir('/Users/Home/Desktop/DePaul/Winter - DSC - 450 - Databases for Analytics/Week 3/Homework') 
''' to change directory '''




fileOpen = open("animal.txt","r")

animalList = fileOpen.readlines()

newlist = []

for line in animalList:
    newLine = line[:-1]
    thisLine = newLine.split(",")
 
  
    print ("["+thisLine[0]+",'"+thisLine[1]+"',"+"'"+thisLine[2]+"',"+thisLine[3]+"]")
    newLine = ("["+thisLine[0]+",'"+thisLine[1]+"',"+"'"+thisLine[2]+"',"+thisLine[3]+"]")
    #print(newLine)
    newlist.append(newLine)
    
print (newlist)

cursor = conn.cursor()
cursor.executemany("INSERT INTO Animal  VALUES (?,?,?,?);", newlist)

newResult = cursor.execute('SELECT * FROM Animal')
newResult.fetchall()