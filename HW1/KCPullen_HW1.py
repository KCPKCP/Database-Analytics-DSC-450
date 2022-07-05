# -*- coding: utf-8 -*-
"""
Keiland Pullen

Winter 2022
DSC 450: Database Processing for Large-Scale Analytics
Assignment Module 1

"""

#Name of Text file for testing
filename = "sample_text.txt";


def avgFileNumbers(filename):
    ''' Part 1 A)
        This function will accept a name of a text file containing multiple
        rows with comma separated numbers and return the average of these
        numbers.
    '''
    
    #Open file for reading
    fp = open(filename, "r");
    
    #Read each line into a variable
    fileRows = fp.readlines();

    #Variables to used for counting number of numbers and average of those numbers.
    TotalNumber = 0;
    TotalValue = 0;

    for row in fileRows:
        # print rows to ensure they are correct
        #print (row);
    
        # convert rows to list and remove trailing newline character
        newRow = row.split(', ');
        newRow[-1] = newRow[-1].replace("\n","")
        # print(newRow);  # Print updated row to ensure that it is correct
    
        # convert each item from string to int
        newRowNums = [int(i) for i in newRow]
        #print(newRowNums) # Print updated row
        
        # calculate sum of each item in list
        SumValue = sum(newRowNums);
        #print(SumValue);  # print sum of each row
    
        # calculate the sum of each line
        TotalValue = TotalValue + SumValue;
    
        # calcuate the length of each row
        rowLength = len(newRow);
    
        # caluclate the total number of numbers in the file
        TotalNumber = TotalNumber + rowLength;
    
        # calculate the average of the all numbers in the file
        avgVal = TotalValue / TotalNumber;
        
    return avgVal;
    

def sqlInsert(tableInfo, studentInfo=[]):
    ''' Part 1 B)
        This function will generate and return a SQL INSERT statement given a
        table name and value list as parameters.
        
        The input parameters are 1 string variable and an array/list
    '''
    
    # print("Table Info ==> " + tableInfo ); # Print table info to ensure that it is correct
    # print(studentInfo);

    infoValues = (str(studentInfo).strip('[]').replace("'","") );
    # print(infoValues); # Print values to ensure there are no brackets or single quotes
    
    return print("INSERT INTO ",tableInfo, "VALUES(",infoValues,");");
    