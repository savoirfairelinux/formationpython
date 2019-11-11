def pair_impair(strs):
        for s in strs:
            if int(s) % 2 == 0:
                print('pair')
            else:
                print('impair')

pair_impair(['1', '2', '3'])