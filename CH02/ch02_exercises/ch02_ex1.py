
def getIsOdd(value):
    modulo = int(value) % 2
    if modulo == 0:
        return False
    else:
        return True

def printIfOddForValues(values):
    for value in values:
        isOdd = getIsOdd(value)
        if isOdd == True:
            print("odd")
        else:
            print("even")
        

printIfOddForValues(["2", "3", "4"])