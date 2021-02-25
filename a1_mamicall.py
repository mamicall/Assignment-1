#!/usr/bin/env python3
''' This script will take the input, filter out the relevant information,
and output that information in the desired format.

OPS435 Assignment 1 - Winter 2021
Program: a1_mamicall.py
Author: Michael Micallef
The python code in this file (a1_mamicall.py) is original work written by
Michael Micallef. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''

import os
import sys

def leap_year(obj):
    '''
    This function will check if the year is a leap year and return "True"
    if it is and "False" if it is not.
    '''
    if (obj % 4 == 0):
        if (obj % 100 == 0):
            if (obj % 400 ==0):
                is_leapyear = True
            else:
                is_leapyear = False
        else:
            is_leapyear = True
    else:
        is_leapyear = False
    		
    return is_leapyear




def sanitize(obj1,obj2):
    '''
    This function will compare the characters in obj1 against the characters in 
    obj2, and filter out the characters that are not in obj2. It will then return
    the sanitized string.
    '''
    
    dob = ""
    for i in obj1:
        if i in obj2:
            dob = dob + i
   
    return dob




def size_check(obj, intobj):
    '''
    This function will compare the inpute data against a number representing
    the required number of characters inputted. 
    '''
     
    if len(obj) == intobj:
        return True
    else:
        return False

    



def range_check(obj1, obj2):
    '''
    This function will compare the date provided against an accepted range, 
    and return "true" if it is within range and "false" if it is not. 
    '''
    rang = tuple(obj2)
    
    if obj1 < rang[0] and obj1 > rang[1]:
        return False
    else: 
        return True
    
    



def usage():    
    '''
    This functon will describe the correct usage of the script.   
    '''    
    
    return("Usage: a1_mamicall.py YYYMMMDD|YYY/MM/DD|YYY-MM-DD|YYY.MM.DD")
   
    
    
    
if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
       
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong data entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: Wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print("Your date of birth is:", new_dob)  

