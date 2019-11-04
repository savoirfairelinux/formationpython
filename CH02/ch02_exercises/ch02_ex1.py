"""
Write a function that takes as a parameter a list of integers as a string (eg ['1', '2', '3'] ) and which displays
for each number whether it is even or odd.
"""

def display_odd_or_even(number_ist):
    for number in number_ist:
        if number % 2 == 0:
            print('{} even'.format(number))
        else:
            print('{} odd'.format(number))
