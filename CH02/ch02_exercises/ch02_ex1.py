def pair_impair(lst):
    for i in lst:
        if int(i) % 2 == 0:
            print("pair")
        else:
            print("impair")    

pair_impair(['6', '7', '8'])