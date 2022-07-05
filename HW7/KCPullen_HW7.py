# -*- coding: utf-8 -*-
"""
Keiland Pullen

Winter 2022
DSC 450: Database Processing for Large-Scale Analytics
Assignment Module 7
"""

import numpy as np
import pandas as pd

def ranNumList(x):
    
    numList = []

    for i in range(0,x):
        ranNum = np.random.randint(33, 100)
        numList.append(ranNum)
    
    #return print(numList)
    return numList


numberList = ranNumList(70)
print(numberList)

numSeries = pd.Series(numberList)
filter = numSeries < 37
numSeries2 = numSeries[filter]
result = numSeries2.count()
 
print("\n")
print(numSeries[filter])
print("\n")
print("There are ",result," of numbers below 37.")
print("\n")


numberArray = np.reshape(numberList, (7,10))
numberArray2 = np.where(numberArray >= 50, 50, numberArray)

print(numberArray)
print("\n")
print(numberArray2) 

