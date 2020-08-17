"""
DD/MM/YYYY format
Days range from 01 to 31 [01-31]
months range from 01 to 12 [01-12]
years range from 1000 to 2999. [1000-2999]
Note that if the day or month is a single digit, it’ll have a leading zero.

month, 
day, and
year, 

and write additional code that can detect if it is a valid date. 
April, June, September, and November have 30 days, 
February has 28 days, 
and the rest of the months have 31 days. 
February has 29 days in leap years. 
Leap years are every year evenly divisible by 4, 
except for years evenly divisible by 100, 
unless the year is also evenly divisible by 400. 
Note how this calculation makes it impossible to make a reasonably sized 
regular expression that can detect a valid date.
"""

import re

datesRegex = re.compile(r"\d\d/\d\d/\d\d\d\d")  # DD/MM/YYYY
mo = datesRegex.search("20/12/2020")

print("The date is: " + mo.group())
