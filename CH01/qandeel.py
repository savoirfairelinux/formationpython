def main(grade):
    if grade <= 100 and grade >= 90:
        result = 'A'
    elif grade <= 89 and grade >= 80:
        result = 'B'
    elif grade <= 79 and grade >= 70:
        result = 'C'
    elif grade <= 69 and grade >= 60:
        result = 'D'
    elif grade < 60:
        result = 'F'
    print(f'Grade is ({result})')

if __name__ == "__main__":
    main(50)
    main(60)
    main(70)
    main(80)
    main(90)
