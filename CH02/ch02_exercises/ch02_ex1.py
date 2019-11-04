def pair_impair(odd_even_list):
    for i in odd_even_list:
        if int(i) % 2 == 0:
            print("pair")
            continue
        print("impair")
