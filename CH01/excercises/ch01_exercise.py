def determine_grade(score):
    if score in range(90, 101):
        return 'A'
    elif score in range(80, 90):
        return 'B'
    elif score in range(70, 80):
        return 'C'
    elif score in range(60, 70):
        return 'D'
    elif score in range(0, 60):
        return 'F'
    else:
        return f'{score } is invalid'

print(determine_grade(score=90))

