# -*- coding: utf-8 -*-
"""
Keiland Pullen

Winter 2022
DSC 450: Database Processing for Large-Scale Analytics
Midterm
"""

import sqlite3

StudentTable = '''CREATE TABLE Student(
StudentID	Number(20) Primary Key,
Name    VARCHAR2(125),
Address	 VARCHAR2(125),
GradYear Number(4)
);
'''

CourseTable = '''CREATE TABLE Course(
CName    VARCHAR2(50) Primary Key,
Department	 VARCHAR2(50),
Credits Number(2)
);
'''

GradeTable = '''CREATE TABLE Grade(
CName VARCHAR2(50),
StudentID	Number(20),
CGrade    CHAR(2),

CONSTRAINT Course_FK
Foreign KEY (CName)
REFERENCES Course(CName),

CONSTRAINT Student_FK
Foreign KEY (StudentID)
REFERENCES STUDENT(StudentID)
);
'''

HoopSchoolView = '''CREATE VIEW HoopSchool As
SELECT student.studentid, student.name, student.address, student.gradyear, 
 course.cname, course.credits, course.department, 
 grade.cgrade
FROM Student
INNER JOIN Grade
    ON Student.StudentID = Grade.StudentID
INNER JOIN Course   
    ON Course.CName = Grade.CName;
'''
conn = sqlite3.connect("midterm_student.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Student")
cursor.execute(StudentTable)

cursor.execute("DROP TABLE IF EXISTS Course")
cursor.execute(CourseTable)

cursor.execute("DROP TABLE IF EXISTS Grade")
cursor.execute(GradeTable)

cursor.execute("DROP VIEW IF EXISTS HoopSchool")
cursor.execute(HoopSchoolView)

print ("INSERT OR IGNORE INTO Student VALUES(33, 'Larry Bird', 'Indiana State', 2022); ")
print ("INSERT OR IGNORE INTO Student VALUES(23, 'Michael Jordan', 'North Carolina', 2023); ")
print ("INSERT OR IGNORE INTO Student VALUES(32, 'Magic Johnson', 'Michigan State', 2022); ")
print ("INSERT OR IGNORE INTO Student VALUES(24, 'Kobe Bryant', 'Lower Merion', 2025); ")
print ("INSERT OR IGNORE INTO Student VALUES(6, 'LeBron James', 'SVSM Ohio', 2023); ")
print ("INSERT OR IGNORE INTO Student VALUES(34, 'Charles Barkley', 'Auburn', 2024); ")

cursor.execute ("INSERT OR IGNORE INTO Student VALUES(33, 'Larry Bird', 'Indiana State', 2022); ")
cursor.execute ("INSERT OR IGNORE INTO Student VALUES(23, 'Michael Jordan', 'North Carolina', 2023); ")
cursor.execute ("INSERT OR IGNORE INTO Student VALUES(32, 'Magic Johnson', 'Michigan State', 2022); ")
cursor.execute ("INSERT OR IGNORE INTO Student VALUES(24, 'Kobe Bryant', 'Lower Merion', 2025); ")
cursor.execute ("INSERT OR IGNORE INTO Student VALUES(6, 'LeBron James', 'SVSM Ohio', 2023); ")
cursor.execute ("INSERT OR IGNORE INTO Student VALUES(34, 'Charles Barkley', 'Auburn', 2024); ")

print ("INSERT OR IGNORE INTO Course VALUES ('Hoops 101', 'Athletics', 2) ;")
print ("INSERT OR IGNORE INTO Course VALUES ('Shooting 201', 'Basketball', 4) ;")
print ("INSERT OR IGNORE INTO Course VALUES ('Hoops History 101', 'History', 4) ;")
print ("INSERT OR IGNORE INTO Course VALUES ('Rebounding 212', 'Athletics', 4) ;")

cursor.execute ("INSERT OR IGNORE INTO Course VALUES ('Hoops 101', 'Athletics', 2) ;")
cursor.execute ("INSERT OR IGNORE INTO Course VALUES ('Shooting 201', 'Basketball', 4) ;")
cursor.execute ("INSERT OR IGNORE INTO Course VALUES ('Hoops History 101', 'History', 4) ;")
cursor.execute ("INSERT OR IGNORE INTO Course VALUES ('Rebounding 212', 'Athletics', 4) ;")

print ("INSERT OR IGNORE INTO Grade VALUES ('Hoops 101', 23, 'A');")
print ("INSERT OR IGNORE INTO Grade VALUES ('Shooting 201', 33, 'A');")
print ("INSERT OR IGNORE INTO Grade VALUES ('Hoops 101', 24, NULL);")
print ("INSERT OR IGNORE INTO Grade VALUES ('Rebounding 212', 34, 'A');")
print ("INSERT OR IGNORE INTO Grade VALUES ('Rebounding 212', 6, 'B');")
print ("INSERT OR IGNORE INTO Grade VALUES ('Shooting 201', 32, 'B');")
print ("INSERT OR IGNORE INTO Grade VALUES ('Shooting 201', 24, 'B');")

cursor.execute ("INSERT OR IGNORE INTO Grade VALUES ('Hoops 101', 23, 'A');")
cursor.execute ("INSERT OR IGNORE INTO Grade VALUES ('Shooting 201', 33, 'A');")
cursor.execute ("INSERT OR IGNORE INTO Grade VALUES ('Hoops 101', 24, NULL);")
cursor.execute ("INSERT OR IGNORE INTO Grade VALUES ('Rebounding 212', 34, 'A');")
cursor.execute ("INSERT OR IGNORE INTO Grade VALUES ('Rebounding 212', 6, 'B');")
cursor.execute ("INSERT OR IGNORE INTO Grade VALUES ('Shooting 201', 32, 'B');")
cursor.execute ("INSERT OR IGNORE INTO Grade VALUES ('Shooting 201', 24, 'B');")


result1 = cursor.execute("select * from HoopSchool")
#result1.fetchall()
result1File = result1.fetchall()

#print(result1File)
#rint(result1File[1])

f = open("midterm_output.txt", "w")

for Rows in result1File:
    if "NULL" in Rows:
        Rows = Rows.replace("NULL", "None")
    print(Rows)
   
    f.write(", ".join(map(str, Rows)) + "\n")
      
f.close()


conn.commit()
conn.close()



conn = sqlite3.connect("midterm_student.db")

cursor = conn.cursor()

conn.commit()
conn.close()



fd = open("midterm_output.txt", "r")

fd_datafile = fd.readlines()

CourseCredits = {}

for fd_data in fd_datafile:
    # print (fd_data)    
    
    fd_datalist = fd_data.split(',')
    studentID   = fd_datalist[0]
    studentName = fd_datalist[1]
    studentAddr = fd_datalist[2]
    stuGradYear = fd_datalist[3]
    CName       = fd_datalist[4]
    Credits     = fd_datalist[5]
    Department  = fd_datalist[6]
    Grade       = fd_datalist[7]
    
    if (CName) in CourseCredits:
        #print("Yes, Key already in dictionary.")
        if CourseCredits[CName] == Credits:
            print("")
        else:
            print(CName + " " + Credits + " credits :")
            print("This entry violates the CName -> Credits functional dependency: \n")
    else:
        CourseCredits.update({CName:Credits})
    
    #print(CName)
    #print(Credits)
    
print("\n")
print("Course-Credits Dictionary :")
print(CourseCredits)


import statistics

query_dict = {}

for qy_data in fd_datafile:
    print(qy_data)
    
    qy_datalist = qy_data.split(',')
    studentID   = qy_datalist[0]
    studentName = qy_datalist[1]
    studentAddr = qy_datalist[2]
    stuGradYear = qy_datalist[3]
    stuGradYear = int(stuGradYear)
    CName       = qy_datalist[4]
    Credits     = qy_datalist[5]
    Department  = qy_datalist[6]
    Grade       = qy_datalist[7]
    
    if (Department) in query_dict:
        print("Yes, " + Department + " is in list.") 
        query_dict[Department].append(stuGradYear)
        
    else:
        query_dict.update({Department:stuGradYear})
        query_dict[Department] = list()
        query_dict[Department].append(stuGradYear)
        
    print(query_dict)
    print (" --------------------- ")   
 
print ("\n")       
    
for i in query_dict :
    print(i, query_dict[i])
    print(i, statistics.mean(query_dict[i]) )
    print("\n")



    

fd.close()













