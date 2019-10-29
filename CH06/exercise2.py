try:
    print('a')
except:
    print('b')
else:
    print('c')
    raise KeyError()
finally:
    print('d')
