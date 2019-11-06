
def maj_inverser(stringValue):
    newString = ""
    for value in stringValue[::-1]:
        character = value = value.capitalize()
        character.capitalize()
        newString += character
    return newString

print(maj_inverser("abcdefg"))