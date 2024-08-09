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

# Function to determine if the year is a leap year
def leap_year(year: int) -> bool:
    "Return true if the year is a leap year"
    '''
    leap_year() -> True if the year is a leap year, else False
    
    Determines if the given year is a leap year according to the Gregorian calendar rules:
    - Divisible by 400: Leap year
    - Divisible by 100 but not by 400: Not a leap year
    - Divisible by 4 but not by 100: Leap year
    - Not divisible by 4: Not a leap year
    '''
    if year % 400 == 0: # Divisible by 400: Leap year
        return True
    if year % 100 == 0: # Divisible by 100 but not by 400: Not a leap year
        return False
    if year % 4 == 0: # Divisible by 4 but not by 100: Leap year
        return True
    return False 

# Function that determines the maximum number of days in a specified month for a given year
def mon_max(month:int, year:int) -> int:
    "Return the maximum number of days in the given month of the given year"
    # Dictionary to store the number of days in each month
    mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    # Get the number of days in the given month
    days = mon_dict.get(month, 31)
    
    # If the month is February and it's a leap year, set days to 29
    if month == 2 and leap_year(year):
        days = 29
    
    return days

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

    # Determine if the year is a leap year by calling leap_year()
    leap_flag = leap_year(year)
    
    # Get the maximum number of days in the current month by calling mon_max()
    mon_max_days = mon_max(mon, year)

    # If the day exceeds the maximum days in the month, adjust month and year
    if day > mon_max_days:
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

# Function to get the next day
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

def day_of_week(date: str) -> str:
    '''
    day_of_week() -> return the day of the week for the given date
    This function is assumed to be implemented elsewhere.
    '''
    pass  # Placeholder for the actual implementation

def day_count(start_date: str, end_date: str) -> int:
    '''
    Count the number of Saturdays and Sundays between start_date and end_date (inclusive).
    
    start_date and end_date should be in the DD/MM/YYYY format.
    '''
    count = 0
    current_date = start_date
    
    while True:
        # Determine the day of the week for the current date
        day_name = day_of_week(current_date)
        
        # Check if the day is Saturday or Sunday
        if day_name in ["Saturday", "Sunday"]:
            count += 1
        
        # Break the loop if we have reached the end_date
        if current_date == end_date:
            break
        
        # Get the next date
        current_date = after(current_date)
    
    return count


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()  # Check if the correct number of arguments are provided

    start_date = sys.argv[1]
    end_date = sys.argv[2]

    if not valid_date(start_date) or not valid_date(end_date):
        usage()  # Check if the provided dates are valid

    # Ensure the start date is always earlier than the end date
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    # Calculate the number of weekend days in the given period
    weekend_days = day_count(start_date, end_date)
    
    # Print the result
    print(f"The period between {start_date} and {end_date} includes {weekend_days} weekend days.")
