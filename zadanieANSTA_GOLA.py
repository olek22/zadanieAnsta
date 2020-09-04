import decimal
import numpy as np

def generator(string1,string2):
    post_codes = []
    first = string1.split('-')
    first = int(first[0] + first[1])
    second = string2.split('-')
    second = int(second[0] + second[1])
    for x in range(first, second+1):
        toStr = str(x)
        code = toStr[:2] + '-' + toStr[2:]
        post_codes.append(code)
    return post_codes



def findLackingElement(l,n):
    lackingElements = list(set(range(1,n)) - set(l))
    return lackingElements
    

def listDecimalGenerator(first, last, step):
    listDec = []
    for x in np.arange(first, last, step):
        listDec.append(decimal.Decimal(x))
    return listDec

# zadanie 1
generator('79-900','80-155')

# zadanie 2
listDecimalGenerator(2,5.5,0.5)

# zadanie 3
findLackingElement([1, 3, 4, 5, 6, 7, 8], 10)
