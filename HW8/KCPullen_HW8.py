# -*- coding: utf-8 -*-
"""
Keiland Pullen

Winter 2022
DSC 450: Database Processing for Large-Scale Analytics
Assignment Module 8
"""

import pandas as pd

df = pd.read_csv("Employee.txt", header=None, na_filter=False)

#print(df)

df.columns = ["First", "Middle", "Last", "EMP_ID", "Bday", "Address", "City", "State", "Sex", "Salary", "Sup_ID", "Dept_ID"]

allMales = df.where(df['Sex'] == "M" )
allMales = allMales.dropna()

#print(df)
print("All of the male employess  are: ")
print("\n")
print(allMales)

print("\n")
print("---" *10)
print("\n")

allFemale = df.where(df['Sex'] == "F")
allFemale = allFemale.dropna()
#print(allFemale)

highestSalaryFemale = allFemale['Salary'].max()

print("The highest salary for female employees is: ", highestSalaryFemale)

# print(df)

print("\n")
print("---" *10)
print("\n")

df_middle = df.groupby(['Middle', 'Salary'])
tempB = ''
for groups in df_middle:
    mid_init, info = groups
    tempA = mid_init[0]
    
    if tempB != mid_init[0]: 
        print("Middle Initial Group is : ",mid_init[0])
        
    tempB = tempA
            
    print("Salary = ", mid_init[1])

