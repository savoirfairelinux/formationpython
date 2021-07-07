def someFn():
    lst = range(1,10)
    for i in range(len(lst) - 2):
        print(list(lst[i:i+3]))

def someFn2():
    result = [list(range(i, i + 3)) for i in range(1, 8)]
    print(*result, sep = '\n')

someFn2()