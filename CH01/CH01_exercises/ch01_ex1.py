"""
Write a program that calculates and print the final grad of a class like in the example:
‘A’ if the grade is bewtween 90 and 100
‘B’ if the grade is bewtween 80 and 89
‘C’ if the grade is bewtween 70 and 79
‘D’ if the grade is bewtween 60 and 69
‘F’ if the grade is smaller then 60
"""


def print_grade(grade):
    if grade >= 90:
        print('A')
    elif grade >= 80:
        print('B')
    elif grade >= 70:
        print('C')
    elif grade >= 60:
        print('D')
    else:
        print('F')


print_grade(75)
