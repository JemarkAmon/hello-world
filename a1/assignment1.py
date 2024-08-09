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
Description: This program calculates the end date, including the day of the week,
given a start date and a number of days to iterate over. It supports both positive and negative
day counts to move forward or backward in time.
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "Return True if the year is a leap year"
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    "Return the maximum number of days in a given month, considering leap years"
    if month == 2:
        return 29 if leap_year(year) else 28
    mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return mon_dict[month]

def after(date: str) -> str:
    '''
    after() -> date for next day in DD/MM/YYYY string format
    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for years after 1582.
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # Increment the day to get the next day

    mon_max_day = mon_max(mon, year)  # Get the maximum days in the current month
    if day > mon_max_day:  # If day exceeds the maximum, adjust month and year
        day = 1
        mon += 1
        if mon > 12:  # If month exceeds December, adjust year
            mon = 1
            year += 1

    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  # Decrement the day to get the previous day

    if day < 1:  # If day is less than 1, adjust month and year
        mon -= 1
        if mon < 1:  # If month is less than January, adjust year
            mon = 12
            year -= 1
        day = mon_max(mon, year)  # Get the maximum days in the previous month

    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

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
    if num > 0:
        for _ in range(num):
            current_date = after(current_date)
    else:
        for _ in range(abs(num)):
            current_date = before(current_date)
    return current_date

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()  # Check length of arguments

    start_date = sys.argv[1]
    if not valid_date(start_date):
        usage()  # Check if the first argument is a valid date

    try:
        num_days = int(sys.argv[2])
    except ValueError:
        usage()  # Check if the second argument is a valid number (+/-)

    end_date = day_iter(start_date, num_days)  # Get the end date
    day_name = day_of_week(end_date)  # Get the day of the week for the end date
    print(f'The end date is {day_name}, {end_date}.')
