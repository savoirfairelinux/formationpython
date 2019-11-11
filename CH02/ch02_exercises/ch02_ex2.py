def pair_impair(list):
    for i in list:
        if int(i) % 2 == 0:
            print('even')
        else:
            print('odd')
    return
pair_impair(['1', '2', '3'])