def someFn():
    lst = range(1,9)
    for i in range(len(lst) - 3):
        print(list(lst[i:i+3]))

someFn()