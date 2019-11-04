import sys
print (sys.argv)

input_array = sys.argv[1:]

for num in input_array:
    if (int(num) % 2) == 0:
       print("{0} is Even".format(num))
    else:
       print("{0} is Odd".format(num))