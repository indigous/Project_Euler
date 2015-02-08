__author__ = 'inigo'
import numpy as np
import operator

dicNumbers = {}

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


def numberTerms(i):
    global dicNumbers
    counter = 0
    while i != 1:
        if i in dicNumbers:
            counter += dicNumbers[i]
            break
        if isEven(i):
            i /= 2
        else:
            i = 3*i + 1
        counter += 1
    return counter


def main():
    global dicNumbers
    for i in range(1, 1000000):
        dicNumbers[i] = numberTerms(i)
    return dicNumbers

dic = main()
maxTerms = max(dicNumbers.iteritems(), key=operator.itemgetter(1))[0]
print "key = ", maxTerms, "  -->  ", "value = ", dic[maxTerms]