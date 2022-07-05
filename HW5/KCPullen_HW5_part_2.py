# -*- coding: utf-8 -*-
"""
Keiland Pullen

Winter 2022
DSC 450: Database Processing for Large-Scale Analytics
Assignment Module 5

"""

import csv
import sqlite3

RecordTable = '''CREATE TABLE RecordNumber(
 License NUMBER(6),
 Renewed DATE, --MMYYYY
 Status VARCHAR(10),
 Status_date DATE, --MMDDYYYY
 Driver_type CHAR(15),
 License_type VARCHAR(15),
 Original DATE, --MMDDYYYY
 Name CHAR(30),
 Sex CHAR(7),
 Chauffeur_city CHAR(15),
 Record_Num VARCHAR(12) NOT NULL UNIQUE,

 CONSTRAINT Rec_pk
  PRIMARY KEY(Record_Num)
);
'''

ChauffeurTable = '''CREATE TABLE CHAUFFEUR
(
  CHAUFFEURCITY  VARCHAR2(30),
  CHAUFFEURSTATE VARCHAR2(20),
  CONSTRAINT Chauffeur_PK
    PRIMARY KEY(CHAUFFEURCITY)
);'''


conn = sqlite3.connect("ChauffeurDatabase.db")

cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS CHAUFFEUR")
cursor.execute(ChauffeurTable)

cursor.execute("DROP TABLE IF EXISTS RecordNumber")
cursor.execute(RecordTable)

fd = open("Public_Chauffeurs_Short_hw3.csv","r")
readFile = csv.reader(fd)
# for row in reader:
#    print(row)
    
#fd.close()

for line in readFile:
    # print(line)
    license = line[0]
    renewed = line[1]
    status = line[2]
    status_date = line[3]
    driver_type = line[4]
    license_type = line[5]
    original_date = line[6]
    name = line[7]
    sex = line[8]
    chauffeur_city = line[9]
    chauffeur_state = line[10]
    record_num = line[11]
    
    # print(license)
    # print(renewed)
    # print(status)
    # print(status_date)
    # print(driver_type)
    # print(license_type)
    # print(original_date)
    # print(name)
    # print(sex)
    # print(chauffeur_city)
    # print(chauffeur_state)
    # print(record_num)
    
    cursor.execute("INSERT OR IGNORE INTO RecordNumber VALUES (?,?,?,?,?,?,?,?,?,?,?);", 
                   (license, renewed, status, status_date, driver_type, license_type,
                    original_date, name, sex, chauffeur_city, record_num))    

    cursor.execute("INSERT OR IGNORE INTO CHAUFFEUR VALUES (?, ?);"
                   , (chauffeur_city, chauffeur_state))
    
    
HowManyRows = cursor.execute("SELECT COUNT(*) FROM CHAUFFEUR;").fetchall()
for Rows in HowManyRows:
    print(Rows)
    
print ("\n")

HowManyMissingDates = cursor.execute("SELECT COUNT(*) FROM RecordNumber WHERE original = 'NULL'")
for MissingDates in HowManyMissingDates:
    print(MissingDates)
    

conn.commit()
conn.close()    
    
