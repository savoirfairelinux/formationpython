#Exercice3 Pair Impair

def pairOuImpair(*args, **kwargs):
    print(args[0])
    for e in args[0]:
        if int(e) % 2==0:
            print('Pair')
        else:
            print('Impair')

pairOuImpair([4,5,11,3,4,6])

