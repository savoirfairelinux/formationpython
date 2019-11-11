def pair_impair(lst):
    for a in lst:
        if a % 2 == 0:
            print("pair", a)
        else:
            print("impair", a)


pair_impair([1, 2, 3, 4, 5, 6])
