# Bilal Qandeel
# Saviorfairpython Training
# Exercise #2
###

def odd_even(some_list):
    for arg in some_list:
        if (arg % 2 == 0):
            print('Even')
        else:
            print('Odd')


if __name__ == "__main__":
    odd_even([0,1,2,3,4,5])
