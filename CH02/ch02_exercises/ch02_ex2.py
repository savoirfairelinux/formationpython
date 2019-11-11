def someFn():
    lst = range(1,10)
    for i in range(len(lst) - 2):
        print(list(lst[i:i+3]))

someFn()