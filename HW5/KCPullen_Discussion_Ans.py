# -*- coding: utf-8 -*-
"""
Keiland Pullen

Winter 2022
DSC 450: Database Processing for Large-Scale Analytics
Assignment Module 5
"""

student = { 1: ["Jack" ,"Grad"],
            2: ["Jane" ,"UGrad"],
			3: ["Jay"  ,"UGrad"],
			4: ["Karen","Grad"]
		  }
		
enrollment = { 1:100,
			   3:200,
			   2:100,
			   4:100
			  }
			  
course = { 100: ["Introduction to Databases",4],
           200: ["Research Colloquium",2]
		  }

# print (student.items() )
# print (enrollment.items() )
# print (course.items() )
# print (student.keys() )
# print (enrollment.keys() )
# print (course.keys() )

for key,value in student.items():
   if "Jack" in value:
    print(value)
    print(key)
    if key in enrollment.keys():
        enroll = (enrollment.get(key) )
        print(enroll)
        if enroll in course.keys():
            thisCourse = (course.get(enroll))
            print(thisCourse)
    
   