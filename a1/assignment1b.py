#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Fall 2023
Program: assignment1.py 
The python code in this file is original work written by
"Jemark Amon". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Jemark Amon jamon@myseneca.ca
Description: This Python script determines the total number of weekend days (Saturdays and Sundays) between a specified start date and end date.
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "Return true if the year is a leap year"
    # A year is a leap year if it is divisible by 4 and (not divisible by 100 or divisible by 400)
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def mon_max(month:int, year:int) -> int:
    "Returns the maximum day for a given month. Includes leap year check"
    if month == 2:
        return 29 if leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

# Function to get the next day
def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    # Split the input date string into day, month, and year components and convert them to integers
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # Increment the day to get the next day

    # Determine if the year is a leap year
    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year if divisible by 100

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year if divisible by 400
    
    # Dictionary to store the number of days in each month
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    # Set the maximum days in the current month, considering leap years for February
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    # If the day exceeds the maximum days in the month, adjust month and year
    if day > mon_max:
        mon += 1 # Move to the next month
        if mon > 12:
            year += 1 # Move to the next year if December is exceeded
            mon = 1 # Reset month to January
        day = 1  # if tmp_day > this month's max, reset to 1 Reset day to the first day of the new month
    # Format and return the new date in DD/MM/YYYY format
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  # previous day

    if day < 1:
        mon -= 1
        if mon < 1:
            year -= 1
            mon = 12
        day = mon_max(mon, year)
    
    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

def valid_date(date: str) -> bool:
    "Check validity of date"
    try:
        day, mon, year = map(int, date.split('/'))
        if year < 1 or mon < 1 or mon > 12 or day < 1 or day > mon_max(mon, year):
            return False
        return True
    except ValueError:
        return False

def day_iter(start_date: str, num: int) -> str:
    "Iterates from start date by num to return end date in DD/MM/YYYY"
    current_date = start_date
    for _ in range(abs(num)):
        current_date = after(current_date) if num > 0 else before(current_date)
    return current_date

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    try:
        num_days = int(sys.argv[2])
    except ValueError:
        usage()

    if not valid_date(start_date):
        usage()
        sys.exit(1)

    end_date = day_iter(start_date, num_days)
    print(f'The end date is {day_of_week(end_date)}, {end_date}.')
