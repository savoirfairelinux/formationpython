"""
Write a program that calculates and print the final grad of a class like in the example:

‘A’ if the grade is bewtween 90 and 100
‘B’ if the grade is bewtween 80 and 89
‘C’ if the grade is bewtween 70 and 79
‘D’ if the grade is bewtween 60 and 69
‘F’ if the grade is smaller then 60
"""


def calculate_grade(grade: int):
    grade_list = {"A": [90, 100], "B": [80, 89], "C": [70, 79], "D": [60, 69], "F": [0, 59]}

    final_grad = None
    for key in grade_list.keys():
        if grade_list[key][1] >= grade >= grade_list[key][0]:
            final_grad = key

    return final_grad
