try:
    1 / 0
    print('a')
except ImportError as e:
    print(e)
except BaseException:
    print('Not handled error')
else:
    print('c')
finally:
    print('d')
