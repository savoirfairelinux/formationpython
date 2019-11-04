
def print_grade(value):
    print(get_grade(value))

def get_grade(value):
    integerValue = int(value)
    if integerValue > 90: return "A"
    if integerValue > 80: return "B"
    if integerValue > 70: return "C"
    if integerValue > 60: return "D"
    else: return "F"

print_grade(80)